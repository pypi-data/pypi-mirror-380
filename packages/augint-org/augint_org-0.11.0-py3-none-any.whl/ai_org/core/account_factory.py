"""AWS Control Tower Account Factory integration."""

import time
from typing import Any, Optional

from botocore.exceptions import ClientError

from ai_org.core.aws_client import AWSClient


class AccountFactory:
    """Manages Control Tower Account Factory provisioning."""

    def __init__(self, profile: Optional[str] = None, region: Optional[str] = None):
        """Initialize Account Factory client.

        Args:
            profile: AWS profile name
            region: AWS region
        """
        self.aws = AWSClient(profile, region)
        self.service_catalog = self.aws.client("servicecatalog")
        self.org_client = self.aws.client("organizations")
        self._product_id: Optional[str] = None
        self._artifact_id: Optional[str] = None

    def find_account_factory_product(self) -> tuple[str, str]:
        """Find the Control Tower Account Factory product and artifact IDs.

        Returns:
            Tuple of (product_id, provisioning_artifact_id)

        Raises:
            Exception: If Account Factory product not found
        """
        if self._product_id is not None and self._artifact_id is not None:
            return (self._product_id, self._artifact_id)

        try:
            # Search for Control Tower Account Factory product
            response = self.service_catalog.search_products(
                Filters={"FullTextSearch": ["Control Tower Account Factory"]}
            )

            for product in response.get("ProductViewSummaries", []):
                if "Account Factory" in product.get("Name", ""):
                    self._product_id = product["ProductId"]

                    # Get the latest provisioning artifact
                    artifacts = self.service_catalog.list_provisioning_artifacts(
                        ProductId=self._product_id
                    )

                    # Get the active artifact
                    for artifact in artifacts.get("ProvisioningArtifactDetails", []):
                        if artifact.get("Active", False):
                            self._artifact_id = artifact["Id"]
                            # Both are now guaranteed to be non-None
                            assert self._product_id is not None
                            assert self._artifact_id is not None
                            return (self._product_id, self._artifact_id)

                    # If no active artifact, use the latest
                    if artifacts.get("ProvisioningArtifactDetails"):
                        self._artifact_id = artifacts["ProvisioningArtifactDetails"][0]["Id"]
                        # Both are now guaranteed to be non-None
                        assert self._product_id is not None
                        assert self._artifact_id is not None
                        return (self._product_id, self._artifact_id)

            raise Exception("Control Tower Account Factory product not found")

        except ClientError as e:
            raise Exception(
                f"Failed to find Account Factory: {self.aws.handle_error(e, 'Service Catalog error')}"
            ) from e

    def provision_account(
        self,
        name: str,
        email: str,
        ou_name: str,
        sso_email: str,
        sso_first_name: str,
        sso_last_name: str,
        wait: bool = True,
    ) -> str:
        """Create account through Control Tower Account Factory.

        This provisions an account through Service Catalog, which automatically:
        - Creates the AWS account
        - Enrolls it in Control Tower
        - Applies baseline controls
        - Deploys StackSets based on OU

        Args:
            name: Account name
            email: Root email address for the account
            ou_name: Target organizational unit name (e.g., "Workloads", "Sandbox")
            sso_email: SSO user email for initial access
            sso_first_name: SSO user first name
            sso_last_name: SSO user last name
            wait: Whether to wait for provisioning to complete

        Returns:
            Account ID of the created account

        Raises:
            Exception: If account provisioning fails
        """
        try:
            product_id, artifact_id = self.find_account_factory_product()

            # Prepare provisioning parameters
            provisioning_params = [
                {"Key": "AccountName", "Value": name},
                {"Key": "AccountEmail", "Value": email},
                {"Key": "ManagedOrganizationalUnit", "Value": ou_name},
                {"Key": "SSOUserEmail", "Value": sso_email},
                {"Key": "SSOUserFirstName", "Value": sso_first_name},
                {"Key": "SSOUserLastName", "Value": sso_last_name},
            ]

            # Start provisioning
            response = self.service_catalog.provision_product(
                ProductId=product_id,
                ProvisioningArtifactId=artifact_id,
                ProvisionedProductName=f"account-{name}",
                ProvisioningParameters=provisioning_params,
            )

            record_id = response["RecordDetail"]["RecordId"]

            if not wait:
                # Return the record ID for tracking
                return f"provisioning-{record_id}"

            # Wait for provisioning to complete
            return self._wait_for_provisioning(record_id)

        except ClientError as e:
            error_msg = str(e)

            # Check for common errors
            if "InvalidParametersException" in error_msg:
                if "ManagedOrganizationalUnit" in error_msg:
                    raise Exception(
                        f"Invalid OU name '{ou_name}'. Use OU name like 'Workloads' or 'Sandbox', not OU ID."
                    ) from e
                if "Email" in error_msg:
                    raise Exception(f"Invalid email format or email already in use: {email}") from e

            raise Exception(
                f"Failed to provision account: {self.aws.handle_error(e, 'Account Factory error')}"
            ) from e

    def _wait_for_provisioning(self, record_id: str, timeout: int = 1800) -> str:
        """Wait for account provisioning to complete.

        Args:
            record_id: Service Catalog provisioning record ID
            timeout: Maximum wait time in seconds (default 30 minutes)

        Returns:
            Account ID of the provisioned account

        Raises:
            Exception: If provisioning fails or times out
        """
        start_time = time.time()

        while time.time() - start_time < timeout:
            try:
                response = self.service_catalog.describe_record(Id=record_id)
                record = response["RecordDetail"]
                status = record["Status"]

                if status == "SUCCEEDED":
                    # Extract account ID from outputs
                    for output in record.get("RecordOutputs", []):
                        if output.get("OutputKey") == "AccountId":
                            return output["OutputValue"]

                    # If no output, try to find account by name
                    return self._find_account_by_name(record["ProvisionedProductName"])

                if status in ["FAILED", "TERMINATED"]:
                    error_msg = record.get("RecordErrors", [{}])[0].get(
                        "Description", "Unknown error"
                    )
                    raise Exception(f"Account provisioning failed: {error_msg}")

                # Still in progress
                time.sleep(30)

            except ClientError as e:
                if "InvalidParametersException" not in str(e):
                    raise Exception(
                        f"Failed to check provisioning status: {self.aws.handle_error(e, 'Status check error')}"
                    ) from e
                time.sleep(30)

        raise Exception(f"Account provisioning timed out after {timeout} seconds")

    def _find_account_by_name(self, name: str) -> str:
        """Find account ID by name.

        Args:
            name: Account name to search for

        Returns:
            Account ID if found

        Raises:
            Exception: If account not found
        """
        # Remove 'account-' prefix if present
        if name.startswith("account-"):
            name = name[8:]

        try:
            response = self.org_client.list_accounts()
            for account in response.get("Accounts", []):
                if account["Name"] == name:
                    return account["Id"]

            raise Exception(f"Account not found: {name}")

        except ClientError as e:
            raise Exception(
                f"Failed to find account: {self.aws.handle_error(e, 'Organizations error')}"
            ) from e

    def get_enrollment_status(self, account_id: str) -> dict[str, Any]:
        """Get Control Tower enrollment status for an account.

        Args:
            account_id: AWS account ID

        Returns:
            Dictionary with enrollment status information
        """
        try:
            # Check if account exists in Organizations
            account_info = self.org_client.describe_account(AccountId=account_id)
            account = account_info["Account"]

            # Get parent OU
            parents = self.org_client.list_parents(ChildId=account_id)
            parent_id = parents["Parents"][0]["Id"] if parents["Parents"] else None

            enrollment_info = {
                "account_id": account_id,
                "account_name": account["Name"],
                "account_email": account["Email"],
                "account_status": account["Status"],
                "parent_ou": parent_id,
                "enrolled": False,  # Will be updated if we can check Control Tower
                "enrollment_status": "Unknown",
            }

            # Try to check Control Tower enrollment
            # Note: There's no direct API, but we can check for Control Tower resources
            try:
                # Check if account has Control Tower baseline StackSets
                cf_client = self.aws.client("cloudformation", account_id=account_id)
                stacks = cf_client.list_stacks(
                    StackStatusFilter=["CREATE_COMPLETE", "UPDATE_COMPLETE"]
                )

                # Look for Control Tower baseline stacks
                ct_stacks = [
                    s
                    for s in stacks.get("StackSummaries", [])
                    if "AWSControlTower" in s.get("StackName", "")
                ]

                if ct_stacks:
                    enrollment_info["enrolled"] = True
                    enrollment_info["enrollment_status"] = "Enrolled"
                    enrollment_info["control_tower_stacks"] = len(ct_stacks)
                else:
                    enrollment_info["enrollment_status"] = "Not enrolled"

            except Exception:
                # Can't check stacks, leave as unknown
                pass

            return enrollment_info

        except ClientError as e:
            return {
                "account_id": account_id,
                "error": self.aws.handle_error(e, "Failed to get enrollment status"),
            }
