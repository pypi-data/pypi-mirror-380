# StackSet Deployment Pipeline Fix Plan

## Current Situation

### The Pipeline Failure
- Pipeline fails at DNS StackSet creation with error: `Parameters: [SubdomainPrefix] must have values`
- Cost management StackSet deploys successfully with anomaly detection restored
- The failure prevents the pipeline from completing even though the main StackSets work

### What We've Done So Far
1. **Fixed Cost Management Issues**:
   - Enabled Cost Explorer in management account (you clicked "Launch Cost Explorer")
   - Waited for propagation - member accounts can now create budgets
   - Restored anomaly detection features to template with fixes:
     - ServiceAnomalyDetector for service-level monitoring
     - AccountAnomalyDetector using CUSTOM type (fixed LINKED_ACCOUNT enum issue)
     - AnomalySubscription with simple Threshold (removed broken ThresholdExpression)
   - Cost management now deploys successfully to both accounts

2. **Created DNS Delegation System**:
   - Template at `stacksets/05-dns-delegation/template.yaml`
   - CLI command `ai-org dns delegate` for on-demand subdomain setup
   - Designed for manual deployment per account when needed

## The Core Problem

### CloudFormation/StackSet Parameter Hierarchy
```
Template Parameters (Required/Optional defined here)
    �
StackSet Default Parameters (Can provide defaults for template params)
    �
Stack Instance Parameter Overrides (Can override defaults per account)
    �
Actual Stack (Gets final parameter values)
```

### Two Types of StackSets We Need

1. **Auto-Deploy StackSets** (cost-management, pipeline-bootstrap, github-oidc):
   - Create StackSet with default parameters from environment
   - Deploy instances to all accounts in specified OUs
   - Auto-deploy to new accounts joining those OUs
   - Parameters known at deployment time (from env vars)

2. **Manual StackSets** (dns-delegation):
   - Create StackSet without default parameters
   - Do NOT deploy instances automatically
   - Parameters provided later via `ai-org dns delegate` command
   - Each instance gets different parameters (subdomain prefix)

### Why Current Code Fails

The `create_stackset_only()` function:
```python
def create_stackset_only(self, name: str, template_path: Path, parameters: dict[str, str]):
    cf_parameters = [{"ParameterKey": k, "ParameterValue": v} for k, v in parameters.items()]
    # When parameters={}, this becomes Parameters=[] (empty list)
    self.cf.create_stack_set(
        StackSetName=name,
        TemplateBody=template_body,
        Parameters=cf_parameters,  # PROBLEM: Empty list != no parameters
        ...
    )
```

When you pass `Parameters=[]` to CloudFormation, it expects values for all required parameters.
When you don't pass `Parameters` at all, CloudFormation accepts the template with its defined parameters for later use.

## The Proper Fix

### Option 1: Minimal Fix (Quick)
Fix `create_stackset_only()` to conditionally include Parameters:
```python
def create_stackset_only(self, name: str, template_path: Path, parameters: dict[str, str]):
    args = {
        "StackSetName": name,
        "TemplateBody": template_body,
        "Capabilities": ["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"],
        "PermissionModel": "SERVICE_MANAGED",
        "AutoDeployment": {"Enabled": False},
        "CallAs": "SELF"
    }

    # Only include Parameters if we have values
    if parameters:
        args["Parameters"] = [{"ParameterKey": k, "ParameterValue": v}
                             for k, v in parameters.items()]

    self.cf.create_stack_set(**args)
```

### Option 2: Proper Redesign (Better)
Unify both functions into one with configuration:
```python
STACKSET_CONFIG = {
    "org-github-oidc": {
        "template": "02-github-oidc/template.yaml",
        "auto_deploy": True,
        "deploy_to_ous": ["workloads", "sandbox"],
        "parameters": lambda: {"GitHubOrg": GITHUB_ORG, "GitHubRepo": GITHUB_REPO}
    },
    "org-cost-management": {
        "template": "04-cost-management/template.yaml",
        "auto_deploy": True,
        "deploy_to_ous": ["workloads", "sandbox"],
        "parameters": lambda: {
            "BudgetEmail": NOTIFICATIONS_EMAIL,
            "MonthlyBudget": str(BUDGETS_MONTHLY_DEFAULT),
            "AnomalyThreshold": str(BUDGETS_ANOMALY_THRESHOLD)
        }
    },
    "org-dns-delegation": {
        "template": "05-dns-delegation/template.yaml",
        "auto_deploy": False,
        "deploy_to_ous": [],  # Manual deployment only
        "parameters": None  # No default parameters
    }
}

def deploy_stackset(name: str, config: dict):
    """Unified function for all StackSet deployments."""
    # Build creation args
    args = {
        "StackSetName": name,
        "TemplateBody": read_template(config["template"]),
        "Capabilities": ["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"],
        "PermissionModel": "SERVICE_MANAGED",
        "AutoDeployment": {"Enabled": config["auto_deploy"]},
        "CallAs": "SELF"
    }

    # Add parameters if provided
    if config["parameters"]:
        params = config["parameters"]()
        if params:
            args["Parameters"] = format_parameters(params)

    # Create/update StackSet
    if stackset_exists(name):
        cf.update_stack_set(**args)
    else:
        cf.create_stack_set(**args)

    # Deploy instances if configured
    for ou in config["deploy_to_ous"]:
        deploy_instances(name, ou)
```

### Option 3: Remove DNS from Pipeline (Simplest)
Since DNS is only deployed manually via CLI command:
1. Delete lines 443-458 in deploy.py (DNS StackSet creation)
2. Let `ai-org dns delegate` create the StackSet on first use
3. Keep pipeline focused on auto-deployed infrastructure only

## Impact Assessment

### What Works Now
-  Cost management with full anomaly detection (both accounts deployed)
-  Pipeline bootstrap (S3 buckets, roles)
-  GitHub OIDC (authentication for CI/CD)
-  Manual DNS delegation via CLI command

### What Needs Fixing
- L Pipeline fails at DNS StackSet creation
- L Pipeline appears to fail even though core infrastructure is deployed

### Files to Modify

**Option 1 (Minimal)**:
- `/root/projects/aillc-org/scripts/deploy.py` - Fix `create_stackset_only()`

**Option 2 (Redesign)**:
- `/root/projects/aillc-org/scripts/deploy.py` - Replace both functions with unified approach
- Possibly create `/root/projects/aillc-org/scripts/stackset_config.py` for configuration

**Option 3 (Remove DNS)**:
- `/root/projects/aillc-org/scripts/deploy.py` - Remove lines 443-458
- `/root/projects/aillc-org/src/ai_org/commands/dns.py` - Add StackSet creation if not exists

## Recommendation

**Start with Option 1** (minimal fix) to get pipeline working immediately, then consider Option 2 for long-term maintainability.

Option 3 is cleanest conceptually but might confuse users who expect all StackSets to be in the pipeline.

## Next Steps

1. Choose approach (Option 1, 2, or 3)
2. Implement fix
3. Test pipeline deployment
4. Verify all StackSets deploy correctly
5. Document the pattern for future StackSets

## Key Decisions Needed

1. Should DNS StackSet be in the pipeline at all?
2. If yes, should we create it without instances (current intent) or remove entirely?
3. Should we redesign now or patch and redesign later?

## Testing Plan

After fix:
1. Run full deployment pipeline
2. Verify cost management still works
3. Verify DNS StackSet exists (if keeping)
4. Test `ai-org dns delegate` command
5. Create new account and verify auto-deployment works
