"""StackSet management commands."""

from typing import Optional

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from ai_org.core.stackset_manager import StackSetManager

console = Console()


@click.group()
def stackset() -> None:
    """Monitor StackSet deployments."""


@stackset.command()
@click.argument("account-id")
@click.option("--stackset", help="Specific StackSet name (default: all)")
@click.option("--wait", is_flag=True, help="Wait for deployments to complete")
@click.pass_context
def status(ctx: click.Context, account_id: str, stackset: Optional[str], wait: bool) -> None:
    """Check StackSet deployment status for an account.

    \b
    Arguments:
      ACCOUNT-ID    AWS account ID (12 digits)

    \b
    Options:
      --stackset TEXT    Specific StackSet name (default: all)
      --wait            Wait for deployments to complete

    \b
    Examples:
      ai-org stackset status 123456789012
      ai-org stackset status 123456789012 --wait
      ai-org stackset status 123456789012 --stackset org-pipeline-bootstrap
    """
    output = ctx.obj["output"]
    manager = StackSetManager(
        profile=ctx.obj.get("profile"),
        region=ctx.obj.get("region"),
    )

    try:
        if wait:
            output.progress(f"Waiting for StackSet deployments in {account_id}...")
            success = manager.wait_for_deployments(account_id, stackset_name=stackset)
            if success:
                output.success("All StackSets deployed successfully")
            else:
                output.warning("Some StackSets may have failed or are still deploying")

        # Get current status
        statuses = manager.get_deployment_status(account_id, stackset_name=stackset)

        if ctx.obj.get("json"):
            output.json_output(statuses)
        elif statuses:
            output.table(
                statuses,
                columns=["StackSetName", "Status", "StatusReason"],
                title=f"StackSet Status for {account_id}",
            )
        else:
            output.info(f"No StackSets found for account {account_id}")

    except Exception as e:
        output.error(f"Failed to check StackSet status: {e}")
        raise click.ClickException(str(e)) from e


@stackset.command(name="list")
@click.pass_context
def list_stacksets(ctx: click.Context) -> None:
    """List all StackSets in the organization.

    \b
    Example:
      ai-org stackset list
    """
    output = ctx.obj["output"]
    manager = StackSetManager(
        profile=ctx.obj.get("profile"),
        region=ctx.obj.get("region"),
    )

    try:
        stacksets = manager.list_stacksets()

        if ctx.obj.get("json"):
            output.json_output(stacksets)
        elif stacksets:
            output.table(
                stacksets,
                columns=["StackSetName", "Status", "AutoDeployOUs", "Instances"],
                title="Organization StackSets",
            )
        else:
            output.info("No StackSets found")

    except Exception as e:
        output.error(f"Failed to list StackSets: {e}")
        raise click.ClickException(str(e)) from e


@stackset.command()
@click.argument("stackset-name")
@click.pass_context
def describe(ctx: click.Context, stackset_name: str) -> None:
    """Get detailed information about a StackSet.

    \b
    Arguments:
      STACKSET-NAME    Name of the StackSet to describe

    \b
    Example:
      ai-org stackset describe org-acm-certificates
      ai-org stackset describe org-dns-delegation
    """
    output = ctx.obj["output"]
    manager = StackSetManager(
        profile=ctx.obj.get("profile"),
        region=ctx.obj.get("region"),
    )

    try:
        # Get StackSet details
        output.progress(f"Fetching details for {stackset_name}...")

        # Describe the StackSet
        try:
            response = manager.cfn_client.describe_stack_set(
                StackSetName=stackset_name,
                CallAs="SELF" if "org-" in stackset_name else "DELEGATED_ADMIN",
            )
        except Exception as e:
            if "StackSetNotFoundException" in str(e):
                output.error(f"StackSet '{stackset_name}' not found")
                return
            raise

        stackset = response["StackSet"]

        # Display basic information
        output.info(f"\n📦 StackSet: {stackset_name}")
        output.text(f"Description: {stackset.get('Description', 'No description')}")
        output.text(f"Status: {stackset.get('Status', 'UNKNOWN')}")
        output.text(f"Permission Model: {stackset.get('PermissionModel', 'N/A')}")

        # Auto-deployment settings
        auto_deploy = stackset.get("AutoDeployment", {})
        if auto_deploy.get("Enabled"):
            output.text("Auto-Deploy: Enabled")
            output.text(
                f"  • Retain stacks on account removal: {auto_deploy.get('RetainStacksOnAccountRemoval', False)}"
            )

            # Try to get target OUs
            try:
                targets_response = manager.cfn_client.list_stack_set_auto_deployment_targets(
                    StackSetName=stackset_name, CallAs="SELF"
                )
                ou_ids = [t["OrganizationalUnitId"] for t in targets_response.get("Summaries", [])]
                if ou_ids:
                    output.text(f"  • Target OUs: {', '.join(ou_ids)}")
            except Exception:
                pass
        else:
            output.text("Auto-Deploy: Disabled")

        # Parameters
        output.info("\n📝 Parameters:")
        parameters = manager.get_stackset_parameters(stackset_name)
        if parameters:
            for param in parameters:
                output.text(f"\n  • {param['name']} ({param['type']})")
                if param.get("description"):
                    output.text(f"    Description: {param['description']}")
                if param.get("default"):
                    output.text(f"    Default: {param['default']}")
                if param.get("current_value"):
                    output.text(f"    Current: {param['current_value']}")
                if param.get("allowed_values"):
                    output.text(f"    Allowed: {', '.join(param['allowed_values'])}")
        else:
            output.text("  No parameters defined")

        # Stack instances
        output.info("\n🚀 Deployments:")
        try:
            instance_count = manager._count_stack_instances(stackset_name)
            if instance_count > 0:
                output.text(f"  Deployed to {instance_count} account(s)")

                # Show first few instances as examples
                paginator = manager.cfn_client.get_paginator("list_stack_instances")
                page = next(
                    paginator.paginate(
                        StackSetName=stackset_name,
                        MaxResults=5,
                        CallAs="SELF" if "org-" in stackset_name else "DELEGATED_ADMIN",
                    )
                )

                for instance in page.get("Summaries", [])[:3]:
                    output.text(
                        f"  • Account {instance['Account']} - Region {instance['Region']} - Status: {instance['Status']}"
                    )

                if instance_count > 3:
                    output.text(f"  ... and {instance_count - 3} more")
            else:
                output.text("  No deployments yet")
        except Exception:
            output.text("  Unable to fetch deployment information")

        # Recent operations
        output.info("\n📊 Recent Operations:")
        try:
            operations = manager.get_stackset_operations(stackset_name, limit=3)
            if operations:
                for op in operations:
                    output.text(
                        f"  • {op['Action']} - {op['Status']} - {op.get('CreationTime', 'Unknown time')}"
                    )
            else:
                output.text("  No recent operations")
        except Exception:
            output.text("  Unable to fetch operations")

        # Example deployment command
        output.info("\n💡 Example Deployment:")
        example_params = []

        # Special handling for ACM certificates - don't show HostedZoneId
        skip_params = ["Region"]
        if stackset_name == "org-acm-certificates":
            skip_params.append("HostedZoneId")  # Auto-discovered

        for param in parameters[:3]:  # Check first 3 params
            if param["name"] not in skip_params:
                example_params.append(f"--param {param['name']}=<value>")

        if example_params:
            output.text(f"  ai-org stackset deploy <account-id> --stackset {stackset_name} \\")
            # Print params with backslash, except for the last item
            for i, param_str in enumerate(example_params):
                is_last = i == len(example_params) - 1
                # Check if regions will be added for non-ACM
                has_regions = stackset_name != "org-acm-certificates"

                if is_last and not has_regions:
                    output.text(f"    {param_str}")
                else:
                    output.text(f"    {param_str} \\")

            # Only show regions for non-ACM stacksets
            if stackset_name != "org-acm-certificates":
                output.text("    --regions us-east-1,us-west-2")
        else:
            output.text(f"  ai-org stackset deploy <account-id> --stackset {stackset_name}")

        # Add note for ACM certificates
        if stackset_name == "org-acm-certificates":
            output.info("\n📌 Note:")
            output.text("  • HostedZoneId is automatically discovered from the domain name")
            output.text("  • Defaults to us-east-1 region (required for CloudFront)")

    except Exception as e:
        output.error(f"Failed to describe StackSet: {e}")
        raise click.ClickException(str(e)) from e


@stackset.command()
@click.argument("account-id")
@click.option("--stackset", required=True, help="StackSet name to deploy")
@click.option("--param", multiple=True, help="Parameter as key=value (can be used multiple times)")
@click.option(
    "--regions",
    help="Comma-separated list of regions (default: us-east-1 for ACM, us-east-1,us-west-2 for others)",
    default=None,  # We'll set the default based on stackset type
)
@click.option("--yes", "-y", is_flag=True, help="Skip confirmation prompt")
@click.pass_context
def deploy(
    ctx: click.Context,
    account_id: str,
    stackset: str,
    param: tuple[str],
    regions: Optional[str],
    yes: bool,
) -> None:
    """Deploy a StackSet to a specific account.

    \b
    Arguments:
      ACCOUNT-ID    AWS account ID (12 digits)

    \b
    Options:
      --stackset TEXT    StackSet name to deploy (required)
      --param TEXT       Parameter as key=value (can be used multiple times)
      --regions TEXT     Comma-separated regions (default: us-east-1,us-west-2)
      --yes, -y          Skip confirmation prompt

    \b
    Examples:
      # Deploy with interactive parameter prompts
      ai-org stackset deploy 123456789012 --stackset pipeline-bootstrap-stackset

      # Deploy with all parameters provided
      ai-org stackset deploy 123456789012 \\
        --stackset github-oidc-stackset \\
        --param GitHubOrg=myorg \\
        --param RepoPattern=* \\
        --regions us-east-1 \\
        --yes
    """
    output = ctx.obj["output"]
    manager = StackSetManager(
        profile=ctx.obj.get("profile"),
        region=ctx.obj.get("region"),
    )

    try:
        # Set default regions based on stackset type
        if regions is None:
            if stackset == "org-acm-certificates":
                regions = "us-east-1"  # ACM certificates for CloudFront must be in us-east-1
            else:
                regions = "us-east-1,us-west-2"  # Default for other stacksets

        # Parse regions
        region_list = [r.strip() for r in regions.split(",")]

        # Parse provided parameters
        provided_params = {}
        for p in param:
            try:
                key, value = p.split("=", 1)
                provided_params[key] = value
            except ValueError:
                output.error(f"Invalid parameter format: {p}. Use key=value")
                raise click.ClickException(
                    f"Invalid parameter format: {p}. Use key=value"
                ) from None

        # Auto-discover HostedZoneId for ACM certificates if not provided
        if (
            stackset == "org-acm-certificates"
            and "DomainName" in provided_params
            and "HostedZoneId" not in provided_params
        ):
            domain_name = provided_params["DomainName"]
            output.progress(f"Searching for hosted zone {domain_name} in account {account_id}...")

            # Import boto3 for Route53 lookup
            import boto3

            session = (
                boto3.Session(profile_name=ctx.obj.get("profile"))
                if ctx.obj.get("profile")
                else boto3.Session()
            )

            # Use the existing function from dns module
            from ai_org.commands.dns import get_zone_id_by_name

            zone_id = None
            try:
                sts_client = session.client("sts")
                # Assume role in target account (where the zone actually exists)
                assumed_role = sts_client.assume_role(
                    RoleArn=f"arn:aws:iam::{account_id}:role/AWSControlTowerExecution",
                    RoleSessionName="ZoneDiscovery",
                )

                # Create Route53 client with assumed role credentials
                target_route53 = boto3.client(
                    "route53",
                    aws_access_key_id=assumed_role["Credentials"]["AccessKeyId"],
                    aws_secret_access_key=assumed_role["Credentials"]["SecretAccessKey"],
                    aws_session_token=assumed_role["Credentials"]["SessionToken"],
                )

                zone_id = get_zone_id_by_name(target_route53, domain_name)
                if zone_id:
                    provided_params["HostedZoneId"] = zone_id
                    output.success(f"Found hosted zone: {zone_id}")
                else:
                    output.warning(
                        f"Could not find hosted zone for {domain_name} in account {account_id}"
                    )
                    output.info("The StackSet will attempt auto-discovery via Lambda when deployed")
            except Exception as e:
                output.warning(f"Could not access account {account_id}: {e}")
                output.info("You may need to provide HostedZoneId manually")

        # Get parameter definitions from the StackSet
        output.info(f"Querying {stackset} parameters...")
        param_definitions = manager.get_stackset_parameters(stackset)

        # Collect all parameters (provided + interactive prompts for missing)
        final_params = {}

        if param_definitions and not yes:
            click.echo()
            click.echo("Enter parameters (press Enter for default):")

            for param_def in param_definitions:
                param_name = param_def["name"]

                # Skip if already provided via CLI
                if param_name in provided_params:
                    final_params[param_name] = provided_params[param_name]
                    continue

                # Build prompt text
                prompt_text = param_name
                if param_def.get("description"):
                    prompt_text = f"{param_name} - {param_def['description']}"

                # Determine default value
                default_value = param_def.get("current_value") or param_def.get("default")

                # Interactive prompt
                if default_value:
                    value = click.prompt(
                        prompt_text,
                        default=default_value,
                        show_default=True,
                    )
                else:
                    value = click.prompt(
                        prompt_text,
                        default="",
                        show_default=False,
                    )
                    if not value:
                        continue  # Skip if no value provided and no default

                final_params[param_name] = value
        else:
            # Use only provided parameters
            final_params = provided_params

        # Show confirmation unless --yes is provided
        if not yes:
            click.echo()

            # Create confirmation table
            table = Table(show_header=False, box=None)
            table.add_column(style="cyan", width=20)
            table.add_column()

            table.add_row("StackSet:", stackset)
            table.add_row("Account:", account_id)
            table.add_row("Regions:", ", ".join(region_list))

            if final_params:
                table.add_row("", "")  # Empty row for spacing
                table.add_row("Parameters:", "")
                for key, value in final_params.items():
                    table.add_row(f"  • {key}:", value)

            panel = Panel(
                table,
                title="[bold yellow]DEPLOYMENT CONFIRMATION[/bold yellow]",
                border_style="yellow",
                padding=(1, 2),
            )
            console.print(panel)

            click.echo()
            if not click.confirm("Proceed with deployment?"):
                output.warning("Deployment cancelled")
                return

        # Execute deployment
        output.progress(f"Deploying {stackset} to account {account_id}...")

        operation_id = manager.deploy_to_account(
            account_id=account_id,
            stackset_name=stackset,
            parameters=final_params,
            regions=region_list,
        )

        output.info(f"Deployment started. Operation ID: {operation_id}")

        # Wait for deployment to complete
        output.progress("Waiting for deployment to complete...")

        success = manager.wait_for_deployment_operation(
            stackset_name=stackset,
            operation_id=operation_id,
            timeout=600,
        )

        if success:
            output.success(f"Successfully deployed {stackset} to account {account_id}")

            # Show final status
            statuses = manager.get_deployment_status(account_id, stackset_name=stackset)
            if statuses:
                output.table(
                    statuses,
                    columns=["StackSetName", "Status", "StatusReason"],
                    title="Deployment Status",
                )
        else:
            output.error("Deployment failed or timed out")

            # Show current status
            statuses = manager.get_deployment_status(account_id, stackset_name=stackset)
            if statuses:
                output.table(
                    statuses,
                    columns=["StackSetName", "Status", "StatusReason"],
                    title="Current Status",
                )

    except Exception as e:
        output.error(f"Failed to deploy StackSet: {e}")
        raise click.ClickException(str(e)) from e
