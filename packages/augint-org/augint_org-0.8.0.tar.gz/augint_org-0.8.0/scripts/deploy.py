#!/usr/bin/env python3
"""
Deploy StackSets and SCPs to AWS Organizations.
Cross-platform deployment script for organization infrastructure.
"""

import os
import sys
import time
from pathlib import Path
from typing import Optional

import boto3
import click
from botocore.exceptions import ClientError
from dotenv import load_dotenv

# Import bootstrap to ensure OUs exist
from .bootstrap import OrgBootstrap

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from src.ai_org.utils.config_loader import create_example_user_config, load_config_value

# Load environment variables
load_dotenv()

# Create example user config on first run
create_example_user_config()

# Configuration with fallback to user config
GITHUB_ORG = load_config_value("GH_ACCOUNT")
GITHUB_REPO = load_config_value("GH_REPO")
NOTIFICATIONS_EMAIL = load_config_value("NOTIFICATIONS_EMAIL")
BUDGETS_MONTHLY_DEFAULT = load_config_value("BUDGETS_MONTHLY_DEFAULT")
BUDGETS_ANOMALY_THRESHOLD = load_config_value("BUDGETS_ANOMALY_THRESHOLD")

# AWS Configuration
HOME_REGION = "us-east-1"
DEPLOYMENT_REGIONS = ["us-east-1"]  # Expand as needed
ALLOWED_REGIONS = ["us-east-1", "us-west-2"]

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
STACKSETS_DIR = PROJECT_ROOT / "stacksets"


class OrgDeployer:
    """Handles deployment of organization infrastructure."""

    def __init__(self, profile: Optional[str] = None):
        """Initialize AWS clients."""
        self.profile = profile
        session = boto3.Session(profile_name=profile) if profile else boto3.Session()
        self.cf = session.client("cloudformation", region_name=HOME_REGION)
        self.org = session.client("organizations")
        self.sts = session.client("sts")

        # Get account info
        identity = self.sts.get_caller_identity()
        self.account_id = identity["Account"]
        self.account_arn = identity["Arn"]

    def get_ou_structure(self) -> dict[str, str]:
        """Get OU structure directly from AWS (without creating or enabling anything)."""
        # Just query existing OU IDs without running bootstrap operations
        bootstrap = OrgBootstrap(profile=self.profile)
        return bootstrap.get_ou_ids_only()

    def deploy_stackset(
        self,
        name: str,
        template_path: Path,
        parameters: dict[str, str],
        ou_id: str,
        permission_model: str = "SERVICE_MANAGED",
    ) -> None:
        """Deploy or update a StackSet."""
        click.echo(f"  • {name}", nl=False)

        with open(template_path, encoding="utf-8") as f:
            template_body = f.read()

        # Format parameters for CloudFormation
        cf_parameters = [{"ParameterKey": k, "ParameterValue": v} for k, v in parameters.items()]

        # Check if StackSet exists
        try:
            self.cf.describe_stack_set(StackSetName=name)
            exists = True
        except ClientError as e:
            if "StackSetNotFoundException" in str(e):
                exists = False
            else:
                raise

        if exists:
            # Update existing StackSet
            try:
                operation_id = self.cf.update_stack_set(
                    StackSetName=name,
                    TemplateBody=template_body,
                    Parameters=cf_parameters,
                    Capabilities=["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"],
                    CallAs="SELF",
                )["OperationId"]
                self._wait_for_operation(name, operation_id)
                click.echo(" ✓")
            except ClientError as e:
                if "No updates are to be performed" in str(e):
                    click.echo(" (current)")
                else:
                    click.echo(f" ✗ {e}")
                    raise
        else:
            # Create new StackSet
            if permission_model == "SERVICE_MANAGED":
                self.cf.create_stack_set(
                    StackSetName=name,
                    TemplateBody=template_body,
                    Parameters=cf_parameters,
                    Capabilities=["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"],
                    PermissionModel="SERVICE_MANAGED",
                    AutoDeployment={"Enabled": True, "RetainStacksOnAccountRemoval": False},
                    CallAs="SELF",
                )
            else:
                # SELF_MANAGED for management account only
                self.cf.create_stack_set(
                    StackSetName=name,
                    TemplateBody=template_body,
                    Parameters=cf_parameters,
                    Capabilities=["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"],
                    PermissionModel="SELF_MANAGED",
                )
            click.echo(" ✓ (created)")

        # Deploy instances for SERVICE_MANAGED StackSets only
        if permission_model == "SERVICE_MANAGED" and ou_id:
            self._deploy_instances(name, ou_id)

    def _deploy_instances(self, stackset_name: str, ou_id: str) -> None:
        """Deploy StackSet instances to an OU."""
        # Check for existing instances in this OU
        instances = self.cf.list_stack_instances(StackSetName=stackset_name, CallAs="SELF")

        # Check if already deployed to this OU
        for instance in instances.get("Summaries", []):
            if instance.get("OrganizationalUnitId") == ou_id:
                click.echo("  ✅ Instances already deployed to OU")
                return

        click.echo("  🚀 Deploying instances to OU...")
        try:
            operation_id = self.cf.create_stack_instances(
                StackSetName=stackset_name,
                DeploymentTargets={"OrganizationalUnitIds": [ou_id]},
                Regions=DEPLOYMENT_REGIONS,
                CallAs="SELF",
            )["OperationId"]
            self._wait_for_operation(stackset_name, operation_id)
            click.echo("  ✅ Instances deployed successfully")
        except ClientError as e:
            if "StackSetNotFoundException" in str(e):
                click.echo("  ⚠️  StackSet not found, skipping instance deployment")
            else:
                raise

    def deploy_management_stack(
        self, name: str, template_path: Path, parameters: dict[str, str]
    ) -> None:
        """Deploy a regular CloudFormation stack to the management account."""
        click.echo(f"  • {name}", nl=False)

        with open(template_path, encoding="utf-8") as f:
            template_body = f.read()

        # Format parameters for CloudFormation
        cf_parameters = [{"ParameterKey": k, "ParameterValue": v} for k, v in parameters.items()]

        # Check if stack exists
        try:
            self.cf.describe_stacks(StackName=name)
            exists = True
        except ClientError as e:
            if "does not exist" in str(e):
                exists = False
            else:
                raise

        try:
            if exists:
                # Update existing stack
                try:
                    self.cf.update_stack(
                        StackName=name,
                        TemplateBody=template_body,
                        Parameters=cf_parameters,
                        Capabilities=["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"],
                    )
                    click.echo(" ✓ (updated)")
                    # Wait for update to complete
                    waiter = self.cf.get_waiter("stack_update_complete")
                    waiter.wait(StackName=name, WaiterConfig={"MaxAttempts": 60})
                except ClientError as e:
                    if "No updates are to be performed" in str(e):
                        click.echo(" ✓ (current)")
                    else:
                        click.echo(f" ✗ {e}")
                        raise
            else:
                # Create new stack
                self.cf.create_stack(
                    StackName=name,
                    TemplateBody=template_body,
                    Parameters=cf_parameters,
                    Capabilities=["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"],
                )
                click.echo(" ✓ (created)")
                # Wait for creation to complete
                waiter = self.cf.get_waiter("stack_create_complete")
                waiter.wait(StackName=name, WaiterConfig={"MaxAttempts": 60})

        except Exception as e:
            click.echo(f" ✗ Failed: {e}")
            raise

    def _verify_pipeline_role(self) -> None:
        """Verify the GitHub Actions pipeline role exists."""
        try:
            # Check if the pipeline role stack exists
            self.cf.describe_stacks(StackName="org-pipeline-role")
            click.echo("✅ Pipeline role verified (for GitHub Actions)")
        except ClientError as e:
            if "does not exist" in str(e):
                click.echo("\n⚠️  WARNING: GitHub Actions pipeline role not found!")
                click.echo("   This is OK for local development, but GitHub Actions will fail.")
                click.echo("   To set up GitHub Actions:")
                click.echo("   1. Run: make setup")
                click.echo("   2. Copy the role ARN from output")
                click.echo(
                    "   3. Add to GitHub: gh secret set AWS_ROLE_ARN --body 'arn:aws:iam::YOUR_ACCOUNT:role/OrgPipelineRole'"
                )
                click.echo("")
            else:
                # Some other error - let it continue
                pass

    def _wait_for_operation(
        self, stackset_name: str, operation_id: str, timeout: int = 300
    ) -> None:
        """Wait for a StackSet operation to complete."""
        start = time.time()
        while time.time() - start < timeout:
            operation = self.cf.describe_stack_set_operation(
                StackSetName=stackset_name, OperationId=operation_id
            )
            status = operation["StackSetOperation"]["Status"]

            if status == "SUCCEEDED":
                return
            if status in ["FAILED", "STOPPED"]:
                raise Exception(f"Operation {operation_id} {status}")

            time.sleep(5)

        raise TimeoutError(f"Operation {operation_id} timed out")

    def create_stackset_only(
        self, name: str, template_path: Path, parameters: dict[str, str]
    ) -> None:
        """Create a StackSet without deploying instances."""
        click.echo(f"  • {name}", nl=False)

        with open(template_path, encoding="utf-8") as f:
            template_body = f.read()

        # Format parameters for CloudFormation
        cf_parameters = [{"ParameterKey": k, "ParameterValue": v} for k, v in parameters.items()]

        # Check if StackSet exists
        try:
            self.cf.describe_stack_set(StackSetName=name)
            exists = True
        except ClientError as e:
            if "StackSetNotFoundException" in str(e):
                exists = False
            else:
                raise

        if exists:
            # Update existing StackSet
            try:
                operation_id = self.cf.update_stack_set(
                    StackSetName=name,
                    TemplateBody=template_body,
                    Parameters=cf_parameters,
                    Capabilities=["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"],
                    CallAs="SELF",
                )["OperationId"]
                self._wait_for_operation(name, operation_id)
                click.echo(" ✓ (updated)")
            except ClientError as e:
                if "No updates are to be performed" in str(e):
                    click.echo(" ✓ (current)")
                else:
                    click.echo(f" ✗ {e}")
                    raise
        else:
            # Create new StackSet without auto-deployment
            self.cf.create_stack_set(
                StackSetName=name,
                TemplateBody=template_body,
                Parameters=cf_parameters,
                Capabilities=["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"],
                PermissionModel="SERVICE_MANAGED",
                AutoDeployment={"Enabled": False},  # Don't auto-deploy
                CallAs="SELF",
            )
            click.echo(" ✓ (created)")

    def deploy_scp(self, ou_id: str) -> None:
        """Deploy Service Control Policy to Workloads OU."""
        click.echo("\n🔒 Deploying Service Control Policy")

        scp_path = STACKSETS_DIR / "scps" / "workloads-baseline.json"
        with open(scp_path) as f:
            policy_content = f.read()

        # Check for existing policy
        policies = self.org.list_policies(Filter="SERVICE_CONTROL_POLICY")
        policy_id = None

        for policy in policies["Policies"]:
            if policy["Name"] == "workloads-baseline":
                policy_id = policy["Id"]
                click.echo(f"  ♻️  Updating existing policy: {policy_id}")
                self.org.update_policy(PolicyId=policy_id, Content=policy_content)
                break

        if not policy_id:
            click.echo("  🆕 Creating new policy...")
            response = self.org.create_policy(
                Name="workloads-baseline",
                Description="Baseline security controls for workload accounts",
                Type="SERVICE_CONTROL_POLICY",
                Content=policy_content,
            )
            policy_id = response["Policy"]["PolicySummary"]["Id"]
            click.echo(f"  ✅ Created policy: {policy_id}")

        # Check if already attached
        attached_policies = self.org.list_policies_for_target(
            TargetId=ou_id, Filter="SERVICE_CONTROL_POLICY"
        )

        already_attached = any(p["Id"] == policy_id for p in attached_policies["Policies"])

        if not already_attached:
            click.echo(f"  🔗 Attaching policy to {ou_id}...")
            self.org.attach_policy(PolicyId=policy_id, TargetId=ou_id)
            click.echo("  ✅ Policy attached")
        else:
            click.echo("  ✅ Policy already attached")

    def deploy_all(self) -> None:
        """Deploy all StackSets and SCPs."""
        if not NOTIFICATIONS_EMAIL:
            click.echo("❌ ERROR: NOTIFICATIONS_EMAIL not set", err=True)
            click.echo("💡 Set it via:", err=True)
            click.echo(
                "  • Environment: export NOTIFICATIONS_EMAIL=your-email@example.com", err=True
            )
            click.echo("  • .env file: NOTIFICATIONS_EMAIL=your-email@example.com", err=True)
            sys.exit(1)

        # Verify pipeline role exists (for GitHub Actions)
        self._verify_pipeline_role()

        # Get OU structure from cache (assuming bootstrap was already run)
        ou_structure = self.get_ou_structure()

        workloads_ou = ou_structure.get("workloads")
        sandbox_ou = ou_structure.get("sandbox")

        if not workloads_ou:
            click.echo("❌ Workloads OU not found. Run 'make bootstrap' first.", err=True)
            return

        # Deploy core StackSets to both Workloads and Sandbox OUs
        click.echo("\n" + "=" * 60)
        click.echo("  STEP 3: STACKSETS & POLICIES")
        click.echo("=" * 60)
        click.echo("\n📦 Deploying infrastructure:")

        # Core StackSets for all accounts (Workloads + Sandbox)
        core_stacksets = [
            {
                "name": "org-github-oidc",
                "template": "02-github-oidc/template.yaml",
                "parameters": {"GitHubOrg": GITHUB_ORG, "RepoPattern": "*", "BranchPattern": "*"},
            },
            {
                "name": "org-pipeline-bootstrap",
                "template": "01-pipeline-bootstrap/template.yaml",
                "parameters": {},
            },
            {
                "name": "org-cost-management",
                "template": "04-cost-management/template.yaml",
                "parameters": {
                    "BudgetEmail": NOTIFICATIONS_EMAIL,
                    "MonthlyBudget": str(BUDGETS_MONTHLY_DEFAULT),
                    "BudgetThreshold": "80",
                    "AnomalyThreshold": str(BUDGETS_ANOMALY_THRESHOLD),
                },
            },
        ]

        # Deploy to both Workloads and Sandbox OUs
        target_ous = [("Workloads", workloads_ou)]
        if sandbox_ou:
            target_ous.append(("Sandbox", sandbox_ou))

        for ou_name, ou_id in target_ous:
            click.echo(f"\n🎯 Deploying to {ou_name} OU:")
            for stackset in core_stacksets:
                template_path = STACKSETS_DIR / stackset["template"]
                if template_path.exists():
                    self.deploy_stackset(
                        name=stackset["name"],
                        template_path=template_path,
                        parameters=stackset["parameters"],
                        ou_id=ou_id,
                    )
                else:
                    click.echo(f"⚠️  Template not found: {template_path}", err=True)

        # Note: Monitoring (03) and log-aggregation (06) are kept for manual deployment
        # when applications exist. They are not auto-deployed to new accounts.

        # Create DNS StackSet (without deploying instances)
        click.echo("\n📦 Creating DNS StackSet (instances deployed on-demand):")
        dns_stackset = {
            "name": "org-dns-delegation",
            "template": "05-dns-delegation/template.yaml",
            "parameters": {},  # Parameters provided during instance creation
        }
        template_path = STACKSETS_DIR / dns_stackset["template"]
        if template_path.exists():
            self.create_stackset_only(
                name=dns_stackset["name"],
                template_path=template_path,
                parameters=dns_stackset["parameters"],
            )
        else:
            click.echo(f"⚠️  DNS template not found: {template_path}", err=True)

        # Deploy SCP to Workloads OU
        self.deploy_scp(workloads_ou)

        click.echo("\n✅ Deployment complete!")
        click.echo(f"   📧 Notifications → {NOTIFICATIONS_EMAIL}")
        click.echo(f"   💰 Budget alerts → ${BUDGETS_MONTHLY_DEFAULT}/month")
        click.echo("   🚀 New accounts auto-provision based on OU placement")

    def destroy_all(self) -> None:
        """Destroy all StackSets and SCPs (cleanup)."""
        click.confirm("⚠️  This will destroy all organization infrastructure. Continue?", abort=True)

        # Get Workloads OU
        roots = self.org.list_roots()
        root_id = roots["Roots"][0]["Id"]
        ous = self.org.list_organizational_units_for_parent(ParentId=root_id)

        ou_id = None
        for ou in ous["OrganizationalUnits"]:
            if ou["Name"] == "Workloads":
                ou_id = ou["Id"]
                break

        if not ou_id:
            click.echo("No Workloads OU found, nothing to destroy")
            return

        # Delete StackSet instances and StackSets
        stackset_names = [
            "cost-management",
            "monitoring-baseline",
            "github-oidc",
            "pipeline-bootstrap",
        ]

        for name in stackset_names:
            try:
                click.echo(f"🗑️  Removing {name}...")

                # Delete instances first
                operation_id = self.cf.delete_stack_instances(
                    StackSetName=name,
                    DeploymentTargets={"OrganizationalUnitIds": [ou_id]},
                    Regions=DEPLOYMENT_REGIONS,
                    RetainStacks=False,
                )["OperationId"]
                self._wait_for_operation(name, operation_id)

                # Delete StackSet
                self.cf.delete_stack_set(StackSetName=name)
                click.echo(f"  ✅ Removed {name}")
            except ClientError as e:
                if "StackSetNotFoundException" in str(e):
                    click.echo(f"  ⚠️  {name} not found")
                else:
                    click.echo(f"  ❌ Error: {e}")

        click.echo("\n✅ Cleanup complete")


@click.command()
@click.option("--destroy", is_flag=True, help="Destroy all infrastructure")
@click.option("--profile", default=os.getenv("AWS_PROFILE"), help="AWS profile to use")
def main(destroy: bool, profile: str):
    """Deploy organization infrastructure to AWS."""
    # Validate required environment variables
    global GITHUB_ORG, GITHUB_REPO, BUDGETS_MONTHLY_DEFAULT, BUDGETS_ANOMALY_THRESHOLD

    if not GITHUB_ORG:
        click.echo("❌ Error: GH_ACCOUNT is required", err=True)
        click.echo("Set via one of:", err=True)
        click.echo("  • .env file in project", err=True)
        click.echo("  • export GH_ACCOUNT=YourGitHubOrg", err=True)
        click.echo("  • ~/.aillc/.env.aillc-org", err=True)
        sys.exit(1)

    if not GITHUB_REPO:
        click.echo("❌ Error: GH_REPO is required", err=True)
        click.echo("Set via one of:", err=True)
        click.echo("  • .env file in project", err=True)
        click.echo("  • export GH_REPO=YourRepoName", err=True)
        click.echo("  • ~/.aillc/.env.aillc-org", err=True)
        sys.exit(1)

    # Apply defaults for optional variables
    if not BUDGETS_MONTHLY_DEFAULT:
        BUDGETS_MONTHLY_DEFAULT = 1000
    else:
        BUDGETS_MONTHLY_DEFAULT = int(BUDGETS_MONTHLY_DEFAULT)

    if not BUDGETS_ANOMALY_THRESHOLD:
        BUDGETS_ANOMALY_THRESHOLD = 100
    else:
        BUDGETS_ANOMALY_THRESHOLD = int(BUDGETS_ANOMALY_THRESHOLD)

    try:
        deployer = OrgDeployer(profile=profile)

        if destroy:
            deployer.destroy_all()
        else:
            deployer.deploy_all()

    except Exception as e:
        click.echo(f"❌ ERROR: {e}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
