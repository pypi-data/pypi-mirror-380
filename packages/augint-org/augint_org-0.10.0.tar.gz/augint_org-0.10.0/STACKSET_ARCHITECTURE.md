# StackSet Architecture Documentation

## Overview

This document describes the unified StackSet deployment architecture implemented for the AILLC organization's AWS Control Tower landing zone.

## Architecture Design

### 1. Registry-Based Configuration

All StackSets are defined in a central registry (`scripts/stackset_registry.py`) that provides:
- Single source of truth for all StackSet configurations
- Declarative deployment behavior
- Priority-based deployment ordering
- Clear separation of auto-deploy and manual StackSets

### 2. Deployment Modes

#### Auto-Deploy StackSets
- Automatically deployed to specified OUs
- New accounts in these OUs receive StackSets automatically
- Examples: pipeline-bootstrap, github-oidc, cost-management

#### Manual-Deploy StackSets
- Created without instances
- Deployed on-demand via CLI or Console
- Parameters provided at deployment time
- Examples: dns-delegation, monitoring, log-aggregation

### 3. Registry Structure

Each StackSet in the registry contains:
```python
{
    "template": "path/to/template.yaml",
    "deployment_mode": "auto|manual",
    "target_ous": ["workloads", "sandbox"],  # For auto-deploy
    "parameters": {...},  # Static or None for manual
    "priority": 1,  # Deployment order
    "description": "What this StackSet does"
}
```

## Implementation Details

### Unified Deployment Method

The `deploy_stackset_unified()` method handles both deployment modes:
- Creates StackSet with or without parameters
- Configures auto-deployment based on mode
- Deploys instances only for auto-deploy StackSets
- Handles the parameter edge case correctly (no Parameters key when None)

### Key Benefits

1. **Scalability**: Easy to add new StackSets to the library
2. **Flexibility**: Support for different deployment patterns
3. **Maintainability**: Clean separation of configuration and logic
4. **Clarity**: Clear understanding of what deploys where and when

## Usage

### Deploying All StackSets
```bash
poetry run python -m scripts.deploy
```

### Adding a New StackSet

1. Create the CloudFormation template in `stacksets/`
2. Add entry to the registry in `stackset_registry.py`
3. Set appropriate deployment mode and target OUs
4. Run deployment script

### Manual StackSet Deployment

For DNS delegation:
```bash
ai-org dns delegate "Account Name" --prefix subdomain
```

For other manual StackSets, use AWS Console or CLI with the created StackSet.

## Future Enhancements

The registry includes examples of future StackSets that can be added:
- GuardDuty threat detection
- AWS Backup policies
- VPC baseline configuration
- X-Ray tracing setup
- Tag compliance policies

## Migration Notes

### Changed Files
1. `scripts/stackset_registry.py` - New registry configuration
2. `scripts/deploy.py` - Updated with unified deployment method
3. Old methods (`deploy_stackset`, `create_stackset_only`) retained for compatibility

### Testing
- Registry validation ensures configuration consistency
- Test script (`scripts/test_registry.py`) validates configuration
- No syntax errors in updated deployment script

## Conclusion

This architecture provides a robust, scalable foundation for managing a curated library of StackSets with different deployment patterns and target OUs. The registry pattern ensures consistency while allowing flexibility for various use cases.
