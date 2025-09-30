"""Account management commands."""

from typing import Optional

import click

from ai_org.core.account_factory import AccountFactory
from ai_org.core.account_manager import AccountManager
from ai_org.core.ou_manager import OUManager


@click.group()
def account() -> None:
    """Manage AWS accounts in the organization."""


@account.command()
@click.argument("name")
@click.argument("email")
def create(name: str, email: str) -> None:
    """Create a new AWS account (NOT IMPLEMENTED).

    \b
    Arguments:
      NAME    Account name (e.g., "Staging LandlineScrubber")
      EMAIL   Root email address for the account
    """
    raise click.ClickException(
        "Account creation via CLI is not currently implemented.\n"
        "\nPlease create accounts manually via Control Tower console:\n"
        "1. Go to AWS Control Tower → Account Factory\n"
        "2. Create account with desired name and email\n"
        "3. Wait for provisioning to complete (20-30 mins)\n"
        "4. Use 'ai-org dns delegate <account-name> --prefix <prefix>' for DNS\n"
        "\nExample: ai-org dns delegate 'Staging LandlineScrubber' --prefix lls"
    )


@account.command(name="list")
@click.option("--ou", help="Filter by OU ID")
@click.option("--status", default="ACTIVE", help="Filter by status (ACTIVE, SUSPENDED)")
@click.option("--no-tree", is_flag=True, help="Don't show OU tree structure")
@click.pass_context
def list_accounts(ctx: click.Context, ou: Optional[str], status: str, no_tree: bool) -> None:
    """List accounts in the organization.

    \b
    Examples:
      ai-org account list
      ai-org account list --ou ou-55d0-workloads
      ai-org account list --status SUSPENDED
      ai-org account list --no-tree  # Skip OU tree display
    """
    output = ctx.obj["output"]
    manager = AccountManager(
        profile=ctx.obj.get("profile"),
        region=ctx.obj.get("region"),
    )

    try:
        # Show OU structure first (unless --no-tree or --json)
        if not no_tree and not ctx.obj.get("json"):
            ou_manager = OUManager(
                profile=ctx.obj.get("profile"),
                region=ctx.obj.get("region"),
            )
            try:
                ou_tree = ou_manager.get_ou_tree()
                output.info("Organization Structure:")
                tree_str = ou_manager.format_ou_tree(ou_tree)
                output.text(tree_str)
                output.text("")  # Empty line for spacing
            except Exception:
                # If we can't get OU tree, just skip it
                pass

        # Get accounts with OU information
        accounts = manager.list_accounts_with_ou(ou=ou, status=status)

        if ctx.obj.get("json"):
            output.json_output(accounts)
        else:
            # Format OU path for display
            for account in accounts:
                # Build OU path
                if account.get("ParentType") == "ROOT":
                    account["OU"] = "Root"
                elif account.get("ParentName"):
                    account["OU"] = account["ParentName"]
                else:
                    account["OU"] = account.get("ParentId", "Unknown")

            output.table(
                accounts,
                columns=["Id", "Name", "Email", "Status", "OU"],
                title=f"AWS Accounts ({status})",
            )
    except Exception as e:
        output.error(f"Failed to list accounts: {e}")
        raise click.ClickException(str(e)) from e


@account.command()
@click.argument("account-id")
@click.pass_context
def get(ctx: click.Context, account_id: str) -> None:
    """Get details for a specific account.

    \b
    Arguments:
      ACCOUNT-ID    AWS account ID (12 digits)

    \b
    Example:
      ai-org account get 123456789012
    """
    output = ctx.obj["output"]
    manager = AccountManager(
        profile=ctx.obj.get("profile"),
        region=ctx.obj.get("region"),
    )

    try:
        account = manager.get_account(account_id)
        if ctx.obj.get("json"):
            output.json_output(account)
        else:
            output.dict_display(account, title=f"Account {account_id}")
    except Exception as e:
        output.error(f"Failed to get account: {e}")
        raise click.ClickException(str(e)) from e


@account.command()
@click.argument("account-id")
@click.pass_context
def enrollment_status(ctx: click.Context, account_id: str) -> None:
    """Check Control Tower enrollment status for an account.

    \b
    Arguments:
      ACCOUNT-ID    AWS account ID (12 digits)

    \b
    Example:
      ai-org account enrollment-status 123456789012

    This command checks if an account is enrolled in Control Tower
    and shows the enrollment status and related information.
    """
    output = ctx.obj["output"]
    factory = AccountFactory(
        profile=ctx.obj.get("profile"),
        region=ctx.obj.get("region"),
    )

    try:
        output.progress(f"Checking enrollment status for account {account_id}...")
        status = factory.get_enrollment_status(account_id)

        if ctx.obj.get("json"):
            output.json_output(status)
        else:
            # Display enrollment information
            if "error" in status:
                output.error(f"Error: {status['error']}")
                return

            output.info(f"Account: {status['account_name']} ({status['account_id']})")
            output.info(f"Email: {status['account_email']}")
            output.info(f"Status: {status['account_status']}")
            output.info(f"Parent OU: {status['parent_ou']}")

            if status["enrolled"]:
                output.success(f"✅ Enrollment Status: {status['enrollment_status']}")
                if "control_tower_stacks" in status:
                    output.info(f"Control Tower Stacks: {status['control_tower_stacks']}")
            else:
                output.warning(f"⚠️  Enrollment Status: {status['enrollment_status']}")
                output.info("\nTo enroll this account in Control Tower:")
                output.info("1. Go to the Control Tower console")
                output.info("2. Navigate to Organization > Accounts")
                output.info("3. Find this account and click 'Enroll'")
                output.info("\nOr re-create the account using:")
                output.info(
                    f"  ai-org account create {status['account_name']} {status['account_email']} --ou <OU_NAME>"
                )

    except Exception as e:
        output.error(f"Failed to check enrollment status: {e}")
        raise click.ClickException(str(e)) from e
