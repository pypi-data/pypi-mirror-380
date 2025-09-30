# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an AWS Control Tower landing zone implementation using direct StackSets (no CfCT complexity) for automated multi-account provisioning. New accounts receive essential resources automatically based on their OU placement - both Workloads and Sandbox get core pipeline and cost management StackSets.

## Architecture

- **Control Tower Foundation**: Management account hosts Control Tower which manages Audit and Log Archive accounts
- **OU Hierarchy**:
  ```
  Root
  ├── Security (CT managed)
  ├── Sandbox (unrestricted, core StackSets only)
  └── Workloads (SCPs applied, core StackSets)
  ```
- **Direct StackSets**: Automated configurations with auto-deployment based on OU placement

## Key Commands

### Docker-based Development
```bash
make claude           # Launch Claude Code in Docker container
make claude-x         # Launch with skip permissions flag
make join-claude      # Open bash in Claude container
make docker-build     # Build containers
make docker-stop      # Stop containers
```

### StackSet Deployment
```bash
python -m scripts.deploy  # Deploy all StackSets and SCPs
```

## Project Structure

### StackSet Templates (`stacksets/`)
- **01-pipeline-bootstrap/**: S3 bucket and CloudFormation execution role (auto-deployed)
- **02-github-oidc/**: GitHub Actions OIDC provider and SAMDeployRole (auto-deployed)
- **03-monitoring/**: CloudWatch alarms for serverless workloads (manual deployment when apps exist)
- **04-cost-management/**: Budget alerts and cost anomaly detection (auto-deployed)
- **06-log-aggregation/**: Centralized logging to Log Archive (manual deployment when needed)
- **scps/**: Service Control Policies for Workloads OU

### Key Design Patterns

1. **Account Strategy**: Descriptive account names with environment suffix, e.g., `api-portal-staging` and `api-portal-prod`
2. **OU-based Deployment**: Both Workloads and Sandbox get core StackSets; SCPs only apply to Workloads
3. **OIDC Authentication**: GitHub Actions assume `SAMDeployRole` via OIDC (no IAM users/keys)
4. **DNS Pattern**: Production owns apex domain, staging owns subdomain
5. **Auto-deployment**: New accounts automatically receive core StackSets based on OU placement

## Environment Variables

Required for deployment scripts:
- `GITHUB_ORG`: GitHub organization (default: svange)
- `GITHUB_REPO`: Repository name (default: aillc-org)
- `NOTIFICATIONS_EMAIL`: Email for all alerts and notifications
- `BUDGETS_MONTHLY_DEFAULT`: Monthly budget in USD (default: 1000)
- `BUDGETS_ANOMALY_THRESHOLD`: Anomaly alert threshold (default: 100)

## Important Constraints

- **No IAM Users**: Enforced by SCP - only SSO users and OIDC roles permitted
- **Control Tower Ownership**: Do not reimplement features Control Tower manages (CloudTrail, Config, guardrails)
- **Manual Steps Required**: Initial SSO user creation and Control Tower setup are console operations
- **Region Restrictions**: SCPs enforce region allow-list for workload accounts

## StackSet Architecture Patterns

All org-* StackSets use SERVICE_MANAGED permission model with Control Tower's existing roles. This avoids the complexity of managing separate IAM roles for SELF_MANAGED StackSets.

### Deployment Modes

1. **Auto-deploy to entire OU**
   - Set `deployment_mode: "auto"` in registry
   - Set `target_ous: ["workloads", "sandbox"]`
   - Automatically deploys to ALL accounts in those OUs
   - New accounts automatically receive the StackSet
   - Examples: `org-pipeline-bootstrap`, `org-github-oidc`, `org-cost-management`

2. **Manual deploy to specific accounts**
   - Set `deployment_mode: "manual"` in registry
   - Set `target_ous: []` (empty list)
   - Deploy using: `ai-org stackset deploy <account-id> --stackset <name>`
   - Uses parent OU + `AccountFilterType: INTERSECTION` to target single account
   - Examples: `org-dns-delegation`, `org-acm-certificates`, `org-monitoring`

### Creating New StackSets

1. **Create template**: `stacksets/<number>-<name>/template.yaml`
2. **Add to registry**: `scripts/stackset_registry.py`
   ```python
   "org-your-stackset": {
       "template": "XX-your-stackset/template.yaml",
       "deployment_mode": "auto" or "manual",
       "target_ous": ["workloads"] or [],  # Empty for manual
       "parameters": None,  # Or dict of default params
       "priority": 20,  # Lower runs first
       "description": "What this StackSet does",
       # DO NOT set permission_model - defaults to SERVICE_MANAGED
   }
   ```
3. **Run deployment**: `make deploy`

### How SERVICE_MANAGED Deploys to Specific Accounts

When deploying to a specific account with `ai-org stackset deploy`:
1. Gets the parent OU of the target account
2. Deploys to that OU with:
   ```python
   DeploymentTargets={
       "OrganizationalUnitIds": [parent_ou],
       "AccountFilterType": "INTERSECTION",
       "Accounts": [account_id]
   }
   ```
3. This tells CloudFormation: "Deploy to this OU, but ONLY to this specific account"

### Key Points

- **Never use SELF_MANAGED**: Control Tower already provides all needed roles
- **SERVICE_MANAGED works for both patterns**: Auto-deploy to OUs and manual to specific accounts
- **No additional IAM roles needed**: Uses Control Tower's existing infrastructure
- **Consistent architecture**: All org-* StackSets follow the same pattern

## Testing & Validation

After deployment, verify:
1. SCPs attached to Workloads OU (inherited by Production/Staging)
2. StackSet instances created in appropriate accounts
3. Production accounts have backups and log aggregation
4. Staging accounts have pipeline resources but no backups
5. New account creation triggers email notification
