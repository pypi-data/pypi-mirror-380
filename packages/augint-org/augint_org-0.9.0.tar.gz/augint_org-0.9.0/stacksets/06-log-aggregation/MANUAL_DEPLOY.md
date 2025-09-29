# Manual Deployment - Log Aggregation StackSet

This StackSet should be deployed manually when applications exist that generate logs needing centralization.

## When to Deploy
Deploy this StackSet when you have:
- Applications generating CloudWatch logs
- Lambda functions with significant logging
- Services that need centralized log analysis
- Compliance requirements for log retention

## How to Deploy
1. Navigate to AWS CloudFormation Console
2. Go to StackSets
3. Create a new StackSet using `template.yaml` from this directory
4. Deploy to specific accounts that have applications generating logs

## Parameters
- `LogArchiveAccountId`: The AWS account ID of your Log Archive account (from Control Tower)

## Prerequisites
- Control Tower must be set up with a Log Archive account
- The Log Archive account ID must be known

## Note
This is not auto-deployed to new accounts to avoid creating unnecessary log infrastructure for accounts without applications.
