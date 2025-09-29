# AWS Organization Restructuring Plan

## Current Situation

### What Went Wrong with Previous Account (226839593255)
1. **Region Mismatch**: Control Tower was set up with regions (us-east-1, us-east-2, us-west-1) but our SCPs only allowed (us-east-1, us-west-2)
   - This caused "explicit deny in service control policy" errors when Control Tower tried to deploy stacks in us-east-2
   - Account enrollment failed with TAINTED status
   - Landing Zone update failed trying to fix regions

2. **Complex OU Structure**: Nested Production/Staging OUs under Workloads added unnecessary complexity
   - Code had to handle nested OU lookups
   - Different StackSets for different sub-OUs
   - More places for things to fail

3. **Account Factory Issues**:
   - The Staging OU showed as "registered" but had 0 controls enabled
   - Account Factory provisioning failed with VPC baseline errors
   - Accounts created through UI ended up in ERROR/TAINTED state

4. **Over-Engineering**:
   - 7 StackSets when we only needed 3
   - Backup strategy for non-existent databases
   - Monitoring alarms for non-existent Lambda functions
   - Account notifications duplicating Control Tower events

### New Clean Setup
- **Management Account**: 385046010920 (fresh start)
- **Control Tower Regions**: us-east-1, us-west-2 (correct this time!)
- **Existing OUs**: Security (with Audit & Log Archive), Sandbox

## Target Architecture

### Simplified OU Structure
```
Root (o-yh9r5q8ltt)
├── Security (ou-yh9r-1twfsrww) [Control Tower Managed]
│   ├── Audit (account)
│   └── Log Archive (account)
├── Sandbox (ou-yh9r-oeicmi8k) [No restrictions, for experiments]
└── Workloads [TO BE CREATED] [Production-ready accounts]
```

### Account Naming Convention
- Use descriptive names with environment suffix
- Examples: `api-portal-staging`, `api-portal-prod`, `website-prod`
- Both staging and prod accounts go in Workloads OU
- Experimental accounts go in Sandbox OU

## StackSet Strategy

### Auto-Deploy to ALL Accounts (Sandbox + Workloads)
1. **01-pipeline-bootstrap**
   - Creates S3 bucket for SAM/CloudFormation deployments
   - Essential for any automated deployment
   - Auto-deploys to new accounts

2. **02-github-oidc**
   - Enables GitHub Actions to deploy without IAM users
   - Security best practice (no long-lived credentials)
   - Auto-deploys to new accounts

3. **04-cost-management**
   - AWS Budgets to prevent billing surprises
   - Not provided by Control Tower
   - Auto-deploys to new accounts

### Keep for Manual Deployment (When Needed)
1. **03-monitoring**
   - CloudWatch alarms for Lambda, API Gateway, DynamoDB
   - Only useful after applications are deployed
   - Deploy manually to specific accounts with apps

2. **06-log-aggregation**
   - Centralizes application logs to Log Archive account
   - Only needed once applications generate logs
   - Deploy manually when needed

### Delete Completely
1. **05-account-notifications**
   - Redundant - Control Tower already emits events
   - Not essential for operation

2. **07-backup-strategy**
   - Use Control Tower's built-in AWS Backup feature instead
   - Can be enabled through Control Tower console when needed

## Service Control Policies (SCPs)

### Apply to Workloads OU Only
- **workloads-baseline.json** SCP with:
  - Region restrictions (us-east-1, us-west-2 only)
  - No IAM user creation (SSO/OIDC only)
  - Require IMDSv2 for EC2
  - Require encrypted S3 transfers
  - Prevent leaving organization

### Sandbox OU
- No SCPs - unrestricted for experimentation
- Isolated from production workloads

## Complete List of Code Changes Required

### Make Targets Impact Analysis
- `make bootstrap` → scripts/bootstrap.py - needs update to remove Production/Staging
- `make setup` → scripts/org_setup.py - no changes needed (management account only)
- `make deploy` → scripts/deploy.py - needs major update for new OU structure
- `make status` → scripts/status.py - needs update to check new structure
- `make test` → tests/ - multiple test files need updating
- `make clean` → no changes needed (just cleans Python cache)

### 1. scripts/bootstrap.py
**Lines to modify: 124-133, 157-158, 174-175, 181-182, 319**
- Remove Production/Staging child OU creation under Workloads
- Update `get_ou_ids_only()` to not look for production/staging
- Update `create_ou_structure()` to only create Workloads at root
- Fix cache structure to not include production/staging keys
- Update validation to not require production/staging

### 2. scripts/deploy.py
**Lines to modify: 329-331, 332-383, 389, 414-444, 429, 447, 480-502**
- Remove separation of workloads_stacksets vs production_stacksets
- Deploy same 3 core StackSets to both Workloads and Sandbox
- Line 389: Remove 05-account-notifications from production_stacksets
- Line 429: Remove 07-backup-strategy from production_stacksets
- Remove Production-specific deployments (log-aggregation, backup)
- Update SCP deployment to only target Workloads OU
- Fix destroy_all() to handle simplified structure

### 3. scripts/status.py
**Lines to modify: 57, 59, 136-142**
- Line 57, 59: Remove checks for Production/Staging child OUs
- Lines 136-142: Update display to show only Workloads and Sandbox
- Fix readiness check logic to not look for nested OUs

### 4. stacksets/scps/workloads-baseline.json
**Already correct with us-east-1, us-west-2 - no changes needed**

### 5. File System Deletions
```bash
# Delete unused StackSet templates
rm -rf stacksets/05-account-notifications/
rm -rf stacksets/07-backup-strategy/

# Create README for manual deployment StackSets
echo "Deploy manually when applications exist" > stacksets/03-monitoring/MANUAL_DEPLOY.md
echo "Deploy manually when applications exist" > stacksets/06-log-aggregation/MANUAL_DEPLOY.md
```

### 6. CLI Command Updates (src/ai_org/)
**Files to update:**
- src/ai_org/commands/account.py (line 52) - update example in help text
- src/ai_org/commands/ou.py (line 131) - update example in help text
- src/ai_org/core/account_factory.py (lines 99, 148) - update OU name examples
- src/ai_org/cli.py - update help text if needed

### 7. Test Updates
**Files to update:**
- tests/conftest.py (lines 33-39) - remove Production/Staging OU mocks
- tests/integration/test_cli_integration.py (line 38) - update OU references
- tests/unit/test_account_commands.py (line 117) - update OU references

### 8. Documentation Updates
**Files that reference Production/Staging OUs:**
- README.md - update architecture diagram and deployment instructions
- CLAUDE.md - update OU hierarchy description
- docs/architecture.md - update OU structure documentation
- docs/configuration.md - update deployment targets
- docs/getting-started.md - update account creation examples
- planning/SPEC.md - historical document, can leave as-is
- planning/MIGRATION_PLAN.md - historical document, can leave as-is

### 9. GitHub Workflow Compatibility
**File: .github/workflows/infrastructure.yaml**
- ✅ No changes needed - workflow uses `make` targets which call updated scripts
- Workflow will continue to work with simplified structure
- Variables (NOTIFICATIONS_EMAIL, BUDGETS_*) remain the same

### 10. Environment Configuration
**File: .env.example**
- ✅ No changes needed - all variables remain valid
- NOTIFICATIONS_EMAIL - still used by remaining StackSets
- BUDGETS_* variables - still used by 04-cost-management
- GitHub and AWS configurations unchanged

## What We're NOT Changing

These components work correctly and don't need changes:
1. **scripts/org_setup.py** - Pipeline role deployment to management account works fine
2. **stacksets/pipeline-role.yaml** - GitHub OIDC for management account is correct
3. **stacksets/scps/workloads-baseline.json** - Already has correct regions (us-east-1, us-west-2)
4. **stacksets/01-pipeline-bootstrap/** - S3 bucket template is fine
5. **stacksets/02-github-oidc/** - GitHub OIDC template is fine
6. **stacksets/04-cost-management/** - Budget template is fine
7. **Makefile** - All targets still work, just call updated scripts

### 11. Testing Strategy\n**Makefile test targets remain functional:**\n- `make test` - runs all tests with pytest\n- `make test-unit` - unit tests only\n- `make test-integration` - integration tests only\n- `make test-coverage` - coverage report\n- `make pre-commit` - linting and formatting checks\n\n**Test files requiring updates:**\n- Update mock OU structures in tests\n- Remove Production/Staging references\n- Update expected StackSet counts (7 → 3 core)\n\n## Implementation Steps

### Phase 1: Create Workloads OU (Manual - AWS Console)
1. Log into AWS Control Tower Console
2. Go to Organization > Organizational units
3. Create new OU named "Workloads" at root level
4. Wait for registration to complete (shows "Succeeded" state)
5. Verify it appears alongside Security and Sandbox OUs

### Phase 2: Update Code
1. Delete unused StackSet directories
2. Modify bootstrap.py to remove nested OU logic
3. Simplify deploy.py to deploy to both Workloads and Sandbox
4. Update status.py to check simplified structure
5. Update tests to match new structure

### Phase 3: Deploy Infrastructure
1. Run `make bootstrap` to verify OU structure
2. Run `make setup` to ensure pipeline role exists
3. Run `make deploy` to deploy StackSets
4. Run `make status` to verify deployment

### Phase 4: Validation
1. Create test account in Workloads OU via Control Tower Console
2. Verify StackSets auto-deployed (GitHub OIDC, S3 bucket, budgets)
3. Verify SCP restrictions apply (region limits, no IAM users)
4. Create test account in Sandbox OU
5. Verify StackSets auto-deployed but no SCP restrictions

## Benefits of This Approach

1. **Simplicity**: Flat OU structure, fewer StackSets
2. **Flexibility**: Same tools in all accounts, differentiated by OU placement
3. **Security**: Workloads restricted, Sandbox unrestricted
4. **Maintainability**: Less code, fewer edge cases
5. **Reliability**: Fewer moving parts = less to break

## Migration Considerations

### Existing Account Handling
If any accounts exist in the old structure:
1. Move them to appropriate new OU via Control Tower Console
2. StackSets will automatically update based on new OU membership
3. Old StackSet instances will be removed from accounts no longer in target OUs

### Rollback Plan
If issues occur:
1. StackSets can be manually deleted via AWS Console
2. SCPs can be detached without affecting accounts
3. Control Tower baseline remains intact
4. No data or applications are affected by these changes

## Known Decisions to Make

1. **Budget Amounts**: What should the default monthly budget be? ($1000?)
2. **Email Notifications**: Single email for all alerts or per-account?
3. **GitHub Repo Access**: All repos (*) or specific pattern?
4. **Future CLI Usage**: Fix the CLI or stick with Control Tower Console UI?

## Risk Mitigation

- Test all changes in Sandbox OU first
- Keep manual deployment option for additional features
- Document everything for future reference
- Use Control Tower's native features where possible
- Avoid custom solutions unless absolutely necessary

## Post-Change Workflow

### Makefile Commands (Unchanged Interface)
After implementing these changes, the workflow remains the same:
1. `make bootstrap` - Creates/verifies Workloads OU (alongside Security, Sandbox)
2. `make setup` - Deploys pipeline role to management account (unchanged)
3. `make deploy` - Deploys 3 core StackSets + SCPs to appropriate OUs
4. `make status` - Shows simplified OU structure and deployments
5. `make test` - Runs updated tests with new OU expectations
6. `make destroy` - Removes all custom StackSets (leaves Control Tower intact)

### What Changes Under the Hood
- `bootstrap`: No longer creates nested Production/Staging OUs
- `deploy`: Deploys 3 StackSets instead of 7
- `deploy`: Applies SCPs only to Workloads OU
- `status`: Shows flat structure instead of nested
- Tests: Expect simpler OU structure

## Success Criteria

- [ ] Can create account via Control Tower Console UI
- [ ] Account automatically gets GitHub OIDC, S3 bucket, and budgets
- [ ] Workloads accounts respect region/IAM restrictions
- [ ] Sandbox accounts have no restrictions
- [ ] No region mismatch errors
- [ ] No "not enrolled in Control Tower" errors
- [ ] Clean, understandable code structure
