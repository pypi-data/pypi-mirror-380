"""AWS CloudFormation StackSet management."""

import json
import time
from typing import Any, Optional

import yaml
from botocore.exceptions import ClientError

from ai_org.core.aws_client import AWSClient


class StackSetManager:
    """Manages AWS CloudFormation StackSets."""

    def __init__(self, profile: Optional[str] = None, region: Optional[str] = None):
        """Initialize StackSet manager.

        Args:
            profile: AWS profile name
            region: AWS region
        """
        self.aws = AWSClient(profile, region)
        self.cfn_client = self.aws.client("cloudformation")

    def get_deployment_status(
        self, account_id: str, stackset_name: Optional[str] = None
    ) -> list[dict[str, Any]]:
        """Get StackSet deployment status for an account.

        Args:
            account_id: AWS account ID
            stackset_name: Specific StackSet name (optional)

        Returns:
            List of status dictionaries
        """
        try:
            statuses = []

            if stackset_name:
                # Get status for specific StackSet
                stacksets = [stackset_name]
            else:
                # List all StackSets
                stacksets = self._list_all_stacksets()

            for name in stacksets:
                # Determine if this is a service-managed stackset
                is_service_managed = name.startswith("org-")
                call_as = "SELF" if is_service_managed else None

                try:
                    # Get stack instance status
                    if call_as:
                        response = self.cfn_client.describe_stack_instance(
                            StackSetName=name,
                            StackInstanceAccount=account_id,
                            StackInstanceRegion=self.aws.region,
                            CallAs=call_as,
                        )
                    else:
                        response = self.cfn_client.describe_stack_instance(
                            StackSetName=name,
                            StackInstanceAccount=account_id,
                            StackInstanceRegion=self.aws.region,
                        )
                    instance = response["StackInstance"]
                    statuses.append(
                        {
                            "StackSetName": name,
                            "Status": instance.get("Status", "UNKNOWN"),
                            "StatusReason": instance.get("StatusReason", ""),
                            "DriftStatus": instance.get("DriftStatus", "NOT_CHECKED"),
                        }
                    )
                except ClientError as e:
                    if e.response["Error"]["Code"] == "StackInstanceNotFoundException":
                        # Stack instance doesn't exist for this account
                        statuses.append(
                            {
                                "StackSetName": name,
                                "Status": "NOT_DEPLOYED",
                                "StatusReason": "Stack instance not found",
                                "DriftStatus": "NOT_CHECKED",
                            }
                        )
                    else:
                        raise

            return statuses

        except ClientError as e:
            raise Exception(self.aws.handle_error(e, "Failed to get deployment status")) from e

    def wait_for_deployments(
        self,
        account_id: str,
        stackset_name: Optional[str] = None,
        timeout: int = 300,
    ) -> bool:
        """Wait for StackSet deployments to complete.

        Args:
            account_id: AWS account ID
            stackset_name: Specific StackSet name (optional)
            timeout: Maximum wait time in seconds

        Returns:
            True if all deployments succeeded, False otherwise
        """
        start_time = time.time()
        check_interval = 10

        while time.time() - start_time < timeout:
            statuses = self.get_deployment_status(account_id, stackset_name)

            # Check if all are in a terminal state
            all_complete = True
            all_success = True

            for status in statuses:
                state = status["Status"]
                if state in ["PENDING", "RUNNING", "OUTDATED"]:
                    all_complete = False
                    break
                if state not in ["CURRENT", "SUCCEEDED"]:
                    all_success = False

            if all_complete:
                return all_success

            time.sleep(check_interval)

        return False  # Timed out

    def list_stacksets(self) -> list[dict[str, Any]]:
        """List all StackSets in the organization.

        Returns:
            List of StackSet dictionaries with enhanced information
        """
        try:
            stacksets = []
            paginator = self.cfn_client.get_paginator("list_stack_sets")

            for page in paginator.paginate(Status="ACTIVE"):
                for summary in page.get("Summaries", []):
                    stackset_name = summary["StackSetName"]

                    # Get detailed information for each StackSet
                    try:
                        # Try to get more detailed info about auto-deployment
                        detail_response = self.cfn_client.describe_stack_set(
                            StackSetName=stackset_name,
                            CallAs="SELF" if "org-" in stackset_name else "DELEGATED_ADMIN",
                        )
                        stackset_detail = detail_response.get("StackSet", {})
                        auto_deploy_config = stackset_detail.get("AutoDeployment", {})

                        # Get target OUs if auto-deployment is enabled
                        if auto_deploy_config.get("Enabled"):
                            target_ous = self._get_target_ous_names(stackset_name)
                            auto_deploy_info = target_ous if target_ous else "Enabled"
                        else:
                            auto_deploy_info = "-"

                        # Count instances
                        instance_count = self._count_stack_instances(stackset_name)
                        instance_info = (
                            f"{instance_count} account{'s' if instance_count != 1 else ''}"
                            if instance_count > 0
                            else "-"
                        )

                    except Exception:
                        # Fallback to summary info if we can't get details
                        auto_deploy_info = (
                            "Enabled" if summary.get("AutoDeployment", {}).get("Enabled") else "-"
                        )
                        instance_info = "-"

                    stacksets.append(
                        {
                            "StackSetName": stackset_name,
                            "Status": summary.get("Status", "UNKNOWN"),
                            "AutoDeployOUs": auto_deploy_info,
                            "Instances": instance_info,
                        }
                    )

            return stacksets

        except ClientError as e:
            raise Exception(self.aws.handle_error(e, "Failed to list StackSets")) from e

    def _get_target_ous_names(self, stackset_name: str) -> str:
        """Get names of target OUs for auto-deployment.

        Args:
            stackset_name: Name of the StackSet

        Returns:
            Comma-separated OU names or empty string
        """
        try:
            response = self.cfn_client.list_stack_set_auto_deployment_targets(
                StackSetName=stackset_name, CallAs="SELF"
            )

            ou_ids = [target["OrganizationalUnitId"] for target in response.get("Summaries", [])]

            if not ou_ids:
                return ""

            # Map common OU IDs to friendly names
            # This is a simplified mapping - ideally would query Organizations API
            ou_names = []
            for ou_id in ou_ids:
                # Try to map known OUs to friendly names
                if "workload" in ou_id.lower() or ou_id.endswith("WORKLOADS"):
                    ou_names.append("Workloads")
                elif "sandbox" in ou_id.lower() or ou_id.endswith("SANDBOX"):
                    ou_names.append("Sandbox")
                elif "security" in ou_id.lower():
                    ou_names.append("Security")
                else:
                    # For now, just show last part of OU ID
                    ou_names.append(ou_id.split("-")[-1][:8])

            return ", ".join(ou_names)

        except Exception:
            return ""

    def _count_stack_instances(self, stackset_name: str) -> int:
        """Count the number of stack instances for a StackSet.

        Args:
            stackset_name: Name of the StackSet

        Returns:
            Number of stack instances
        """
        try:
            paginator = self.cfn_client.get_paginator("list_stack_instances")
            count = 0

            for page in paginator.paginate(
                StackSetName=stackset_name,
                CallAs="SELF" if "org-" in stackset_name else "DELEGATED_ADMIN",
            ):
                count += len(page.get("Summaries", []))

            return count
        except Exception:
            return 0

    def _list_all_stacksets(self) -> list[str]:
        """List all StackSet names.

        Returns:
            List of StackSet names
        """
        stacksets = []
        paginator = self.cfn_client.get_paginator("list_stack_sets")

        for page in paginator.paginate(Status="ACTIVE"):
            for summary in page.get("Summaries", []):
                stacksets.append(summary["StackSetName"])

        return stacksets

    def get_stackset_operations(self, stackset_name: str, limit: int = 10) -> list[dict[str, Any]]:
        """Get recent operations for a StackSet.

        Args:
            stackset_name: StackSet name
            limit: Maximum number of operations to return

        Returns:
            List of operation dictionaries
        """
        try:
            response = self.cfn_client.list_stack_set_operations(
                StackSetName=stackset_name,
                MaxResults=limit,
            )

            operations = []
            for op in response.get("Summaries", []):
                operations.append(
                    {
                        "OperationId": op["OperationId"],
                        "Action": op.get("Action", "UNKNOWN"),
                        "Status": op.get("Status", "UNKNOWN"),
                        "CreationTime": op.get("CreationTimestamp"),
                        "EndTime": op.get("EndTimestamp"),
                    }
                )

            return operations

        except ClientError as e:
            raise Exception(
                self.aws.handle_error(e, f"Failed to get operations for {stackset_name}")
            ) from e

    def get_stackset_parameters(self, stackset_name: str) -> list[dict[str, Any]]:
        """Get parameter definitions from a StackSet.

        Args:
            stackset_name: Name of the StackSet

        Returns:
            List of parameter definitions with names, types, defaults, and descriptions
        """
        try:
            # Try with DELEGATED_ADMIN first, fall back to default if not delegated
            try:
                response = self.cfn_client.describe_stack_set(
                    StackSetName=stackset_name,
                    CallAs="DELEGATED_ADMIN",
                )
            except ClientError as e:
                if "ValidationError" in str(e):
                    # Not a delegated admin, try without CallAs
                    response = self.cfn_client.describe_stack_set(
                        StackSetName=stackset_name,
                    )
                else:
                    raise

            stackset = response.get("StackSet", {})
            template_body = stackset.get("TemplateBody", "")
            current_params = {
                p["ParameterKey"]: p["ParameterValue"] for p in stackset.get("Parameters", [])
            }

            # Parse template to get parameter definitions
            try:
                # Try parsing as JSON first
                template = json.loads(template_body)
            except json.JSONDecodeError:
                # Fall back to YAML
                try:
                    template = yaml.safe_load(template_body)
                except Exception:
                    # If both fail, return current parameters without definitions
                    return [
                        {
                            "name": key,
                            "type": "String",
                            "default": None,
                            "description": None,
                            "current_value": value,
                        }
                        for key, value in current_params.items()
                    ]

            # Extract parameter definitions from template
            parameters = []
            for param_name, param_def in template.get("Parameters", {}).items():
                parameters.append(
                    {
                        "name": param_name,
                        "type": param_def.get("Type", "String"),
                        "default": param_def.get("Default"),
                        "description": param_def.get("Description"),
                        "allowed_values": param_def.get("AllowedValues"),
                        "current_value": current_params.get(param_name, param_def.get("Default")),
                    }
                )

            return parameters

        except ClientError as e:
            raise Exception(
                self.aws.handle_error(e, f"Failed to get parameters for {stackset_name}")
            ) from e

    def deploy_to_account(
        self,
        account_id: str,
        stackset_name: str,
        parameters: Optional[dict[str, str]] = None,
        regions: Optional[list[str]] = None,
    ) -> str:
        """Deploy a StackSet to a specific account.

        Args:
            account_id: Target AWS account ID
            stackset_name: Name of the StackSet to deploy
            parameters: Parameter overrides as key-value pairs
            regions: List of regions to deploy to (defaults to us-east-1, us-west-2)

        Returns:
            Operation ID for tracking the deployment
        """
        try:
            if not regions:
                regions = ["us-east-1", "us-west-2"]

            # Convert parameters to CloudFormation format
            param_overrides = []
            if parameters:
                for key, value in parameters.items():
                    param_overrides.append({"ParameterKey": key, "ParameterValue": value})

            # For SERVICE_MANAGED StackSets (org-*), we need to deploy to parent OU with account filtering
            is_service_managed = stackset_name.startswith("org-")

            deployment_targets = {}
            call_as: Optional[str] = "SELF"  # Default for service-managed

            if is_service_managed:
                # Get the parent OU for this account
                import boto3

                org_client = boto3.client("organizations")
                parents = org_client.list_parents(ChildId=account_id)
                parent_ou = parents["Parents"][0]["Id"]

                # Deploy to parent OU with account filtering
                deployment_targets = {
                    "OrganizationalUnitIds": [parent_ou],
                    "AccountFilterType": "INTERSECTION",
                    "Accounts": [account_id],
                }
            else:
                # Self-managed stacksets can target accounts directly
                deployment_targets = {"Accounts": [account_id]}
                call_as = "DELEGATED_ADMIN"

            # Check if stack instance already exists
            instance_exists = False
            try:
                self.cfn_client.describe_stack_instance(
                    StackSetName=stackset_name,
                    StackInstanceAccount=account_id,
                    StackInstanceRegion=regions[0],
                    CallAs=call_as,
                )
                instance_exists = True
            except ClientError as check_e:
                if "StackInstanceNotFoundException" not in str(check_e):
                    # Some other error - pass it through
                    pass

            # Create or update stack instances
            try:
                if instance_exists:
                    # Update existing instances
                    response = self.cfn_client.update_stack_instances(
                        StackSetName=stackset_name,
                        DeploymentTargets=deployment_targets,
                        Regions=regions,
                        ParameterOverrides=param_overrides if param_overrides else [],
                        OperationPreferences={
                            "RegionConcurrencyType": "PARALLEL",
                            "MaxConcurrentPercentage": 100,
                        },
                        CallAs=call_as,
                    )
                else:
                    # Create new instances
                    response = self.cfn_client.create_stack_instances(
                        StackSetName=stackset_name,
                        DeploymentTargets=deployment_targets,
                        Regions=regions,
                        ParameterOverrides=param_overrides if param_overrides else [],
                        OperationPreferences={
                            "RegionConcurrencyType": "PARALLEL",
                            "MaxConcurrentPercentage": 100,
                        },
                        CallAs=call_as,
                    )
            except ClientError as e:
                if (
                    not is_service_managed
                    and "ValidationError" in str(e)
                    and "delegated administrator" in str(e)
                ):
                    # Not a delegated admin for self-managed stacksets, try without CallAs
                    call_as = None
                    try:
                        if instance_exists:
                            response = self.cfn_client.update_stack_instances(
                                StackSetName=stackset_name,
                                DeploymentTargets=deployment_targets,
                                Regions=regions,
                                ParameterOverrides=param_overrides if param_overrides else [],
                                OperationPreferences={
                                    "RegionConcurrencyType": "PARALLEL",
                                    "MaxConcurrentPercentage": 100,
                                },
                            )
                        else:
                            response = self.cfn_client.create_stack_instances(
                                StackSetName=stackset_name,
                                DeploymentTargets=deployment_targets,
                                Regions=regions,
                                ParameterOverrides=param_overrides if param_overrides else [],
                                OperationPreferences={
                                    "RegionConcurrencyType": "PARALLEL",
                                    "MaxConcurrentPercentage": 100,
                                },
                            )
                    except ClientError as no_call_as_error:
                        raise Exception(
                            self.aws.handle_error(
                                no_call_as_error, f"Failed to deploy {stackset_name}"
                            )
                        ) from no_call_as_error
                else:
                    raise Exception(
                        self.aws.handle_error(
                            e, f"Failed to deploy {stackset_name} to {account_id}"
                        )
                    ) from e

            return response["OperationId"]

        except ClientError as e:
            raise Exception(
                self.aws.handle_error(e, f"Failed to deploy {stackset_name} to {account_id}")
            ) from e

    def wait_for_deployment_operation(
        self, stackset_name: str, operation_id: str, timeout: int = 600
    ) -> bool:
        """Wait for a StackSet operation to complete.

        Args:
            stackset_name: Name of the StackSet
            operation_id: Operation ID to monitor
            timeout: Maximum wait time in seconds

        Returns:
            True if operation succeeded, False otherwise
        """
        start_time = time.time()
        check_interval = 5

        # Determine if this is a service-managed stackset
        is_service_managed = stackset_name.startswith("org-")
        call_as = "SELF" if is_service_managed else "DELEGATED_ADMIN"

        while time.time() - start_time < timeout:
            try:
                try:
                    response = self.cfn_client.describe_stack_set_operation(
                        StackSetName=stackset_name,
                        OperationId=operation_id,
                        CallAs=call_as,
                    )
                except ClientError as e:
                    if (
                        not is_service_managed
                        and "ValidationError" in str(e)
                        and "delegated administrator" in str(e)
                    ):
                        # Not a delegated admin, try without CallAs
                        response = self.cfn_client.describe_stack_set_operation(
                            StackSetName=stackset_name,
                            OperationId=operation_id,
                        )
                    else:
                        raise

                operation = response.get("StackSetOperation", {})
                status = operation.get("Status")

                if status == "SUCCEEDED":
                    return True
                if status in ["FAILED", "STOPPED"]:
                    return False
                # Status is RUNNING or QUEUED, keep waiting

                time.sleep(check_interval)

            except ClientError as e:
                raise Exception(
                    self.aws.handle_error(e, f"Failed to check operation status for {operation_id}")
                ) from e

        return False  # Timed out
