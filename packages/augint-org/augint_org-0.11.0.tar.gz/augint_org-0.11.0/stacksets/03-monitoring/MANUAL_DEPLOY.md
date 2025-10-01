# Manual Deployment - Monitoring StackSet

This StackSet should be deployed manually when applications exist that need monitoring.

## When to Deploy
Deploy this StackSet when you have:
- Lambda functions that need error monitoring
- API Gateway endpoints that need request/response monitoring
- DynamoDB tables that need throughput monitoring
- Other AWS resources requiring CloudWatch alarms

## How to Deploy
1. Navigate to AWS CloudFormation Console
2. Go to StackSets
3. Create a new StackSet using `template.yaml` from this directory
4. Deploy to specific accounts that have applications needing monitoring

## Parameters
- `AlarmEmail`: Email address for alarm notifications
- `AlarmPrefix`: Prefix for alarm names (e.g., "AppName")
- `LambdaErrorThreshold`: Error count before triggering alarm
- `API4xxThreshold`: 4xx error count threshold
- `API5xxThreshold`: 5xx error count threshold

## Note
This is not auto-deployed to new accounts to avoid creating unnecessary alarms for accounts without applications.
