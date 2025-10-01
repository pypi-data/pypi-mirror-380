#!/usr/bin/env python3
"""Fix manual StackSets by recreating them with SELF_MANAGED permission model."""

import time

import boto3
import click
from botocore.exceptions import ClientError


def delete_stackset_if_exists(cf_client, stackset_name):
    """Delete a StackSet if it exists."""
    try:
        # Check if StackSet exists
        cf_client.describe_stack_set(StackSetName=stackset_name, CallAs="SELF")

        # Check for existing instances
        paginator = cf_client.get_paginator("list_stack_instances")
        instances = []
        for page in paginator.paginate(StackSetName=stackset_name, CallAs="SELF"):
            instances.extend(page.get("Summaries", []))

        if instances:
            click.echo(f"  ⚠️  {stackset_name} has {len(instances)} instances - skipping deletion")
            click.echo(
                "     Please delete instances manually if you want to recreate this StackSet"
            )
            return False

        # Delete the StackSet
        click.echo(f"  🗑️  Deleting {stackset_name}...")
        cf_client.delete_stack_set(StackSetName=stackset_name, CallAs="SELF")

        # Wait for deletion to complete
        while True:
            try:
                cf_client.describe_stack_set(StackSetName=stackset_name, CallAs="SELF")
                time.sleep(2)
            except ClientError as e:
                if "StackSetNotFoundException" in str(e):
                    click.echo(f"  ✅ {stackset_name} deleted")
                    return True
                raise

    except ClientError as e:
        if "StackSetNotFoundException" in str(e):
            click.echo(f"  ℹ️  {stackset_name} doesn't exist")
            return True
        click.echo(f"  ❌ Error checking {stackset_name}: {e}")
        return False


def main():
    """Fix manual StackSets that need SELF_MANAGED permission model."""
    click.echo("\n🔧 Fixing Manual StackSets Permission Models")
    click.echo("=" * 60)

    cf_client = boto3.client("cloudformation", region_name="us-east-1")

    # List of manual StackSets that need to be SERVICE_MANAGED
    manual_stacksets = ["org-monitoring", "org-log-aggregation", "org-acm-certificates"]

    click.echo("\n📋 Checking manual StackSets that need SERVICE_MANAGED permission model:")

    stacksets_to_fix = []
    for stackset_name in manual_stacksets:
        try:
            response = cf_client.describe_stack_set(StackSetName=stackset_name, CallAs="SELF")
            permission_model = response["StackSet"].get("PermissionModel", "SERVICE_MANAGED")

            if permission_model == "SELF_MANAGED":
                click.echo(
                    f"  ⚠️  {stackset_name}: Currently SELF_MANAGED, needs to be SERVICE_MANAGED"
                )
                stacksets_to_fix.append(stackset_name)
            else:
                click.echo(f"  ✅ {stackset_name}: Already SERVICE_MANAGED")

        except ClientError as e:
            if "StackSetNotFoundException" in str(e):
                click.echo(f"  ℹ️  {stackset_name}: Not found (will be created fresh)")
            else:
                click.echo(f"  ❌ {stackset_name}: Error checking - {e}")

    if stacksets_to_fix:
        click.echo(f"\n⚠️  Found {len(stacksets_to_fix)} StackSets that need to be recreated:")
        for name in stacksets_to_fix:
            click.echo(f"  • {name}")

        if click.confirm("\n🔄 Delete and recreate these StackSets?"):
            click.echo("\n🗑️  Deleting StackSets...")
            for stackset_name in stacksets_to_fix:
                delete_stackset_if_exists(cf_client, stackset_name)

            click.echo(
                "\n✅ StackSets deleted. Run 'make deploy' to recreate them with SERVICE_MANAGED permission model."
            )
        else:
            click.echo("\n❌ Cancelled. Manual StackSets remain unchanged.")
    else:
        click.echo("\n✅ All manual StackSets are correctly configured or don't exist yet.")
        click.echo("   Run 'make deploy' to create/update them.")


if __name__ == "__main__":
    main()
