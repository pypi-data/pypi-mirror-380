"""
StackSet Registry - Central configuration for all organization StackSets.

This registry defines the deployment behavior, target OUs, and parameters
for each StackSet in the curated library.
"""

from typing import Any


def get_stackset_registry(
    github_org: str,
    github_repo: str,
    notifications_email: str,
    budgets_monthly_default: int,
    budgets_anomaly_threshold: int,
) -> dict[str, dict[str, Any]]:
    """
    Get the StackSet registry with resolved parameters.

    Args:
        github_org: GitHub organization name
        github_repo: GitHub repository name
        notifications_email: Email for notifications
        budgets_monthly_default: Monthly budget in USD
        budgets_anomaly_threshold: Anomaly detection threshold in USD

    Returns:
        Dictionary of StackSet configurations
    """
    return {
        # Priority 1: Core Infrastructure - Deploy First
        "org-pipeline-bootstrap": {
            "template": "01-pipeline-bootstrap/template.yaml",
            "deployment_mode": "auto",
            "target_ous": ["workloads", "sandbox"],
            "parameters": {},  # No parameters needed
            "priority": 1,
            "description": "S3 buckets and CloudFormation execution role for CI/CD",
        },
        # Priority 2: GitHub OIDC Provider
        "org-github-oidc": {
            "template": "02-github-oidc/template.yaml",
            "deployment_mode": "auto",
            "target_ous": ["workloads", "sandbox"],
            "parameters": {
                "GitHubOrg": github_org,
                "RepoPattern": "*",  # Allow all repos by default
                "BranchPattern": "*",  # Allow all branches by default
            },
            "priority": 2,
            "description": "GitHub Actions OIDC provider and SAMDeployRole",
        },
        # Priority 2.5: API Gateway Logging
        "org-apigateway-logging": {
            "template": "08-apigateway-logging/template.yaml",
            "deployment_mode": "auto",
            "target_ous": ["workloads", "sandbox"],
            "parameters": {},
            "priority": 2,
            "description": "API Gateway CloudWatch Logs role for REST APIs",
        },
        # Priority 3: Cost Management
        "org-cost-management": {
            "template": "04-cost-management/template.yaml",
            "deployment_mode": "auto",
            "target_ous": ["workloads", "sandbox"],
            "parameters": {
                "BudgetEmail": notifications_email,
                "MonthlyBudget": str(budgets_monthly_default),
                "BudgetThreshold": "80",  # Alert at 80% of budget
                "ForecastThreshold": "100",  # Alert when forecast exceeds budget
                "AnomalyThreshold": str(budgets_anomaly_threshold),
            },
            "priority": 3,
            "description": "Budget alerts and cost anomaly detection",
        },
        # Manual Deployment StackSets
        # Monitoring - Deploy when applications exist
        "org-monitoring": {
            "template": "03-monitoring/template.yaml",
            "deployment_mode": "manual",
            "target_ous": [],  # Manually selected during deployment
            "parameters": None,  # Parameters provided at deployment time
            "priority": 10,
            "description": "CloudWatch alarms for serverless applications",
        },
        # DNS Delegation - Deploy for staging/production subdomains
        "org-dns-delegation": {
            "template": "05-dns-delegation/template.yaml",
            "deployment_mode": "manual",
            "target_ous": [],  # Manually selected during deployment
            "parameters": None,  # Parameters provided via CLI (SubdomainPrefix)
            "priority": 11,
            "description": "DNS delegation zones for subdomain management",
            # Uses SERVICE_MANAGED, deploys to account's parent OU
        },
        # Log Aggregation - Deploy for production accounts
        "org-log-aggregation": {
            "template": "06-log-aggregation/template.yaml",
            "deployment_mode": "manual",
            "target_ous": [],  # Manually selected for production accounts
            "parameters": None,  # Parameters may be provided at deployment
            "priority": 12,
            "description": "Centralized logging to Log Archive account",
        },
        # ACM Certificates - Deploy for domains needing SSL/TLS
        "org-acm-certificates": {
            "template": "07-acm-certificates/template.yaml",
            "deployment_mode": "manual",
            "target_ous": [],  # Manually selected during deployment
            "parameters": None,  # Parameters provided via CLI (DomainName, HostedZoneId)
            "priority": 13,
            "description": "ACM wildcard certificates with DNS validation",
        },
    }


# Future StackSets can be added here with their configurations:
# Examples of additional StackSets you might add to your library:

FUTURE_STACKSETS = {
    # Security & Compliance
    "org-guardduty": {
        "template": "07-guardduty/template.yaml",
        "deployment_mode": "auto",
        "target_ous": ["workloads"],  # Not needed in sandbox
        "parameters": None,
        "priority": 4,
        "description": "GuardDuty threat detection",
    },
    # Backup & Recovery
    "org-backup-policies": {
        "template": "08-backup/template.yaml",
        "deployment_mode": "auto",
        "target_ous": ["workloads"],  # Production backups only
        "parameters": None,
        "priority": 5,
        "description": "AWS Backup policies for RDS, EBS, EFS",
    },
    # Networking
    "org-vpc-baseline": {
        "template": "09-vpc/template.yaml",
        "deployment_mode": "manual",
        "target_ous": [],  # Deploy as needed
        "parameters": None,  # CIDR blocks provided at deployment
        "priority": 20,
        "description": "Standard VPC configuration",
    },
    # Developer Tools
    "org-codecommit-repos": {
        "template": "10-codecommit/template.yaml",
        "deployment_mode": "manual",
        "target_ous": [],  # Deploy where needed
        "parameters": None,
        "priority": 21,
        "description": "CodeCommit repository setup",
    },
    # Observability
    "org-xray-tracing": {
        "template": "11-xray/template.yaml",
        "deployment_mode": "auto",
        "target_ous": ["workloads"],
        "parameters": None,
        "priority": 6,
        "description": "X-Ray distributed tracing configuration",
    },
    # Tags & Compliance
    "org-tag-policies": {
        "template": "12-tags/template.yaml",
        "deployment_mode": "auto",
        "target_ous": ["workloads", "sandbox"],
        "parameters": None,
        "priority": 7,
        "description": "Mandatory tagging policies",
    },
}


def validate_registry(registry: dict[str, dict[str, Any]]) -> bool:
    """
    Validate the StackSet registry for consistency.

    Args:
        registry: The StackSet registry to validate

    Returns:
        True if valid, raises exception otherwise
    """
    required_fields = ["template", "deployment_mode", "target_ous", "priority"]

    for name, config in registry.items():
        # Check required fields
        for field in required_fields:
            if field not in config:
                raise ValueError(f"StackSet '{name}' missing required field: {field}")

        # Validate deployment mode
        if config["deployment_mode"] not in ["auto", "manual"]:
            raise ValueError(
                f"StackSet '{name}' has invalid deployment_mode: {config['deployment_mode']}"
            )

        # Validate auto-deploy has target OUs
        if config["deployment_mode"] == "auto" and not config["target_ous"]:
            raise ValueError(f"Auto-deploy StackSet '{name}' must have target_ous defined")

        # Validate manual deploy has empty target OUs
        if config["deployment_mode"] == "manual" and config["target_ous"]:
            raise ValueError(f"Manual-deploy StackSet '{name}' should have empty target_ous")

    return True
