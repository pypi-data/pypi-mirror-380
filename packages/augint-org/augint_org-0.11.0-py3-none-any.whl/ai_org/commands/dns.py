"""DNS management commands for staging environments."""

import time
from typing import Any, Optional

import boto3
import click
from botocore.exceptions import ClientError


@click.group()
def dns() -> None:
    """Manage DNS zones and delegation."""


@dns.command()
@click.argument("account_name")
@click.option("--prefix", required=True, help="Subdomain prefix (e.g., org, lls, api)")
@click.option(
    "--domain", default="aillc.link", help="Root domain for delegation (default: aillc.link)"
)
@click.option(
    "--no-cert",
    is_flag=True,
    help="Skip ACM certificate creation (default: create certificate)",
)
@click.pass_context
def delegate(
    ctx: click.Context, account_name: str, prefix: str, domain: str, no_cert: bool
) -> None:
    """Setup DNS delegation for an account subdomain.

    This command:
    1. Deploys a DNS StackSet to create the subdomain zone
    2. Retrieves the NS records from the new zone
    3. Updates the parent zone with NS delegation
    4. Optionally creates an ACM wildcard certificate for the domain

    \b
    Examples:
        ai-org dns delegate "Staging Augmenting Integrations" --prefix org
        ai-org dns delegate "Staging LandlineScrubber" --prefix lls --no-cert
        ai-org dns delegate "Production API" --prefix api --domain prod.company.com
    """
    output = ctx.obj["output"]
    profile = ctx.obj.get("profile")
    region = ctx.obj.get("region", "us-east-1")

    # Initialize AWS clients
    session = boto3.Session(profile_name=profile) if profile else boto3.Session()
    cf_client = session.client("cloudformation", region_name=region)
    org_client = session.client("organizations")
    route53_client = session.client("route53")

    try:
        # 1. Get account ID from account name
        output.progress(f"Looking up account '{account_name}'...")
        account_id = get_account_id_by_name(org_client, account_name)
        if not account_id:
            _handle_account_not_found(account_name, org_client, output)
            # This line is never reached due to exception in handler, but mypy doesn't know that
            return
        output.success(f"Found account: {account_id}")

        # 2. Deploy DNS StackSet instance
        output.progress(f"Deploying DNS zone for {prefix}.{domain}...")
        deploy_dns_stackset_instance(cf_client, account_id, prefix, domain, region)

        # 3. Wait and get stack outputs
        output.progress("Waiting for stack deployment...")
        time.sleep(10)  # Give it a moment to start
        stack_outputs = get_stack_instance_outputs(cf_client, account_id, region)

        ns_records = stack_outputs["NameServers"].split(",")
        output.success(f"DNS zone created with {len(ns_records)} name servers")

        # 4. Look up parent zone ID
        output.progress(f"Looking up parent zone {domain}...")
        parent_zone_id = get_zone_id_by_name(route53_client, domain)
        if not parent_zone_id:
            _handle_parent_zone_not_found(domain)
            return  # Never reached but satisfies mypy

        # 5. Update parent zone with NS delegation
        output.progress(f"Adding NS delegation for {prefix}.{domain}...")
        add_ns_delegation(route53_client, parent_zone_id, f"{prefix}.{domain}", ns_records)

        output.success("✅ DNS configured successfully!")
        output.info(f"\nDomain: {prefix}.{domain}")
        output.info(f"Account: {account_name} ({account_id})")
        output.info("\nName servers:")
        for ns in ns_records:
            output.text(f"  - {ns}")

        # 6. Optionally deploy ACM certificate
        if not no_cert:
            full_domain = f"{prefix}.{domain}"
            output.progress(f"Deploying ACM certificate for {full_domain} and *.{full_domain}...")
            try:
                subdomain_zone_id = stack_outputs.get("HostedZoneId")
                if not subdomain_zone_id:
                    raise ValueError("Could not retrieve subdomain zone ID from stack outputs")
                deploy_acm_certificate(
                    cf_client, account_id, full_domain, subdomain_zone_id, region
                )
                output.success(f"✅ ACM certificate created for {full_domain} (includes wildcard)")
                output.info(
                    "\nCertificate will be validated automatically via DNS. "
                    "Check ACM console for validation status."
                )
            except Exception as cert_error:
                output.warning(f"Certificate deployment failed: {cert_error}")
                output.info("You can manually deploy the certificate later using:")
                output.text(
                    f"  ai-org stackset deploy {account_id} --stackset org-acm-certificates "
                    f"--param DomainName={full_domain}"
                )

        output.info(f"\nYou can now deploy resources using {prefix}.{domain}")

    except click.ClickException:
        raise
    except Exception as e:
        output.error(f"Failed to setup DNS: {e}")
        raise click.ClickException(str(e)) from e


def _handle_account_not_found(account_name: str, org_client: Any, output: Any) -> None:
    """Handle account not found error."""
    output.error(f"Account '{account_name}' not found")
    list_staging_accounts(org_client, output)
    msg = f"Account '{account_name}' not found"
    raise click.ClickException(msg) from None


def _handle_parent_zone_not_found(domain: str) -> None:
    """Handle parent zone not found error."""
    msg = (
        f"Parent zone {domain} not found in management account. "
        "Please create it first:\n"
        f"  aws route53 create-hosted-zone --name {domain} "
        f"--caller-reference $(date +%s)"
    )
    raise click.ClickException(msg) from None


def get_account_id_by_name(org_client: Any, account_name: str) -> Optional[str]:
    """Get account ID from account name."""
    paginator = org_client.get_paginator("list_accounts")
    for page in paginator.paginate():
        for account in page["Accounts"]:
            if account["Name"] == account_name:
                return account["Id"]
    return None


def list_staging_accounts(org_client: Any, output: Any) -> None:
    """List accounts to help user find the right account name."""
    paginator = org_client.get_paginator("list_accounts")
    accounts = []
    for page in paginator.paginate():
        for account in page["Accounts"]:
            accounts.append(account["Name"])

    output.info("\nAvailable accounts:")
    for name in sorted(accounts)[:10]:  # Show first 10
        output.text(f"  - {name}")
    if len(accounts) > 10:
        output.text(f"  ... and {len(accounts) - 10} more")


def get_zone_id_by_name(route53_client: Any, zone_name: str) -> Optional[str]:
    """Get hosted zone ID from zone name."""
    try:
        response = route53_client.list_hosted_zones_by_name(DNSName=zone_name)
        zone_name = zone_name.rstrip(".")

        for zone in response["HostedZones"]:
            if zone["Name"].rstrip(".") == zone_name:
                # Extract ID from /hostedzone/Z123...
                return zone["Id"].split("/")[-1]
    except ClientError:
        pass
    return None


def deploy_dns_stackset_instance(
    cf_client: Any, account_id: str, prefix: str, root_domain: str, region: str
) -> None:
    """Deploy DNS StackSet instance to an account."""
    stackset_name = "org-dns-delegation"

    # Check if StackSet exists
    try:
        cf_client.describe_stack_set(StackSetName=stackset_name, CallAs="SELF")
    except ClientError:
        raise click.ClickException(
            f"StackSet '{stackset_name}' not found. "
            "Please run 'python -m scripts.deploy' to create it first."
        ) from None

    # Get the parent OU for this account
    import boto3

    org_client = boto3.client("organizations")
    parents = org_client.list_parents(ChildId=account_id)
    parent_ou = parents["Parents"][0]["Id"]

    # Check if instance already exists
    try:
        existing = cf_client.describe_stack_instance(
            StackSetName=stackset_name,
            StackInstanceAccount=account_id,
            StackInstanceRegion=region,
            CallAs="SELF",
        )
        if existing:
            # Update existing instance
            operation_id = cf_client.update_stack_instances(
                StackSetName=stackset_name,
                DeploymentTargets={
                    "OrganizationalUnitIds": [parent_ou],
                    "AccountFilterType": "INTERSECTION",
                    "Accounts": [account_id],
                },
                Regions=[region],
                ParameterOverrides=[
                    {"ParameterKey": "SubdomainPrefix", "ParameterValue": prefix},
                    {"ParameterKey": "RootDomain", "ParameterValue": root_domain},
                ],
                CallAs="SELF",
            )["OperationId"]
    except ClientError as e:
        if "StackInstanceNotFoundException" in str(e):
            # Create new instance
            operation_id = cf_client.create_stack_instances(
                StackSetName=stackset_name,
                DeploymentTargets={
                    "OrganizationalUnitIds": [parent_ou],
                    "AccountFilterType": "INTERSECTION",
                    "Accounts": [account_id],
                },
                Regions=[region],
                ParameterOverrides=[
                    {"ParameterKey": "SubdomainPrefix", "ParameterValue": prefix},
                    {"ParameterKey": "RootDomain", "ParameterValue": root_domain},
                ],
                CallAs="SELF",
            )["OperationId"]
        else:
            raise

    # Wait for operation to complete
    wait_for_stackset_operation(cf_client, stackset_name, operation_id)


def get_stack_instance_outputs(cf_client: Any, account_id: str, region: str) -> dict[str, Any]:
    """Get outputs from a stack instance."""
    stackset_name = "org-dns-delegation"

    # Wait a bit more for stack to be ready
    time.sleep(20)

    # Get stack instance details
    response = cf_client.describe_stack_instance(
        StackSetName=stackset_name,
        StackInstanceAccount=account_id,
        StackInstanceRegion=region,
        CallAs="SELF",
    )

    # Get parameters to know the domain
    params = response["StackInstance"].get("ParameterOverrides", [])
    prefix = next(
        (p["ParameterValue"] for p in params if p["ParameterKey"] == "SubdomainPrefix"), None
    )
    domain = next(
        (p["ParameterValue"] for p in params if p["ParameterKey"] == "RootDomain"), "aillc.link"
    )

    full_domain = f"{prefix}.{domain}"

    # Use STS to assume role in target account to read the stack outputs
    # This uses the AWSControlTowerExecution role that exists in all CT accounts
    import boto3

    sts_client = boto3.client("sts")

    try:
        # Assume the execution role in the target account
        assumed_role = sts_client.assume_role(
            RoleArn=f"arn:aws:iam::{account_id}:role/AWSControlTowerExecution",
            RoleSessionName="DNSStackOutputReader",
        )

        # Create CF client with assumed role credentials
        target_cf_client = boto3.client(
            "cloudformation",
            region_name=region,
            aws_access_key_id=assumed_role["Credentials"]["AccessKeyId"],
            aws_secret_access_key=assumed_role["Credentials"]["SecretAccessKey"],
            aws_session_token=assumed_role["Credentials"]["SessionToken"],
        )

        # Get the actual stack outputs
        stack_id = response["StackInstance"]["StackId"]
        stack_response = target_cf_client.describe_stacks(StackName=stack_id)

        outputs = {}
        if "Outputs" in stack_response["Stacks"][0]:
            for output in stack_response["Stacks"][0]["Outputs"]:
                outputs[output["OutputKey"]] = output["OutputValue"]

        return outputs

    except Exception as e:
        # If we can't assume role, try to get NS records from public DNS after they propagate
        # Wait for DNS propagation
        time.sleep(30)

        # Query Route53 directly in the management account for the zone
        route53 = boto3.client("route53")
        try:
            # List all zones and find the one we just created
            zones = route53.list_hosted_zones()
            for zone in zones["HostedZones"]:
                if zone["Name"].rstrip(".") == full_domain:
                    zone_id = zone["Id"].split("/")[-1]
                    # Get the NS records for this zone
                    records = route53.list_resource_record_sets(
                        HostedZoneId=zone_id, StartRecordType="NS", StartRecordName=full_domain
                    )
                    for record in records["ResourceRecordSets"]:
                        if record["Type"] == "NS" and record["Name"].rstrip(".") == full_domain:
                            ns_records = [r["Value"] for r in record["ResourceRecords"]]
                            return {
                                "NameServers": ",".join(ns_records),
                                "HostedZoneId": zone_id,
                                "FullDomain": full_domain,
                            }
        except Exception:
            pass

        # Last fallback - return placeholder that will need manual intervention
        raise click.ClickException(
            f"Unable to retrieve NS records for {full_domain}. "
            "The zone was created but NS records couldn't be retrieved automatically. "
            "Please check the AWS Console and add NS delegation manually."
        )


def add_ns_delegation(
    route53_client: Any, parent_zone_id: str, subdomain: str, ns_records: list[str]
) -> None:
    """Add NS delegation records to parent zone."""
    route53_client.change_resource_record_sets(
        HostedZoneId=parent_zone_id,
        ChangeBatch={
            "Comment": f"NS delegation for {subdomain}",
            "Changes": [
                {
                    "Action": "UPSERT",
                    "ResourceRecordSet": {
                        "Name": subdomain,
                        "Type": "NS",
                        "TTL": 300,
                        "ResourceRecords": [{"Value": ns} for ns in ns_records],
                    },
                }
            ],
        },
    )


def wait_for_stackset_operation(
    cf_client: Any, stackset_name: str, operation_id: str, timeout: int = 300
) -> None:
    """Wait for a StackSet operation to complete."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        response = cf_client.describe_stack_set_operation(
            StackSetName=stackset_name, OperationId=operation_id, CallAs="SELF"
        )

        status = response["StackSetOperation"]["Status"]
        if status == "SUCCEEDED":
            return
        if status in ["FAILED", "STOPPED"]:
            error_msg = f"StackSet operation {status}"
            raise Exception(error_msg)

        time.sleep(5)

    raise TimeoutError(f"StackSet operation timed out after {timeout} seconds")


def deploy_acm_certificate(
    cf_client: Any, account_id: str, domain_name: str, hosted_zone_id: str, region: str
) -> None:
    """Deploy ACM certificate StackSet instance to an account."""
    stackset_name = "org-acm-certificates"

    # Check if StackSet exists
    try:
        cf_client.describe_stack_set(StackSetName=stackset_name, CallAs="SELF")
    except ClientError:
        raise click.ClickException(
            f"StackSet '{stackset_name}' not found. Please run 'make deploy' to create it first."
        ) from None

    # Get the parent OU for this account
    import boto3

    org_client = boto3.client("organizations")
    parents = org_client.list_parents(ChildId=account_id)
    parent_ou = parents["Parents"][0]["Id"]

    # Check if instance already exists
    try:
        existing = cf_client.describe_stack_instance(
            StackSetName=stackset_name,
            StackInstanceAccount=account_id,
            StackInstanceRegion=region,
            CallAs="SELF",
        )
        if existing:
            # Update existing instance
            operation_id = cf_client.update_stack_instances(
                StackSetName=stackset_name,
                DeploymentTargets={
                    "OrganizationalUnitIds": [parent_ou],
                    "AccountFilterType": "INTERSECTION",
                    "Accounts": [account_id],
                },
                Regions=[region],
                ParameterOverrides=[
                    {"ParameterKey": "DomainName", "ParameterValue": domain_name},
                    {"ParameterKey": "HostedZoneId", "ParameterValue": hosted_zone_id},
                ],
                CallAs="SELF",
            )["OperationId"]
    except ClientError as e:
        if "StackInstanceNotFoundException" in str(e):
            # Create new instance
            operation_id = cf_client.create_stack_instances(
                StackSetName=stackset_name,
                DeploymentTargets={
                    "OrganizationalUnitIds": [parent_ou],
                    "AccountFilterType": "INTERSECTION",
                    "Accounts": [account_id],
                },
                Regions=[region],
                ParameterOverrides=[
                    {"ParameterKey": "DomainName", "ParameterValue": domain_name},
                    {"ParameterKey": "HostedZoneId", "ParameterValue": hosted_zone_id},
                ],
                CallAs="SELF",
            )["OperationId"]
        else:
            raise

    # Wait for operation to complete
    wait_for_stackset_operation(cf_client, stackset_name, operation_id, timeout=180)
