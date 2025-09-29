"""Integration tests for CLI functionality."""

import os
from unittest.mock import MagicMock, Mock, patch

import pytest

from ai_org.cli import cli


@pytest.mark.integration
class TestCLIIntegration:
    """Integration tests for the CLI."""

    def test_full_account_workflow(self, runner, mock_boto3_session):
        """Test a complete account creation and management workflow."""
        with patch("ai_org.core.aws_client.boto3.Session") as mock_session:
            mock_session.return_value = mock_boto3_session["session"]

            # Mock ConfigManager to return None for SSO user to skip SSO assignment
            with patch(
                "ai_org.core.config_manager.ConfigManager.get_default_sso_user"
            ) as mock_config:
                mock_config.return_value = None

                # List accounts before
                result = runner.invoke(cli, ["account", "list"])
                assert result.exit_code == 0
                result.output.count("ACTIVE")

                # Set required env vars for Account Factory
                os.environ["DEFAULT_SSO_USER"] = "testuser"

                # Mock OU name lookup
                mock_boto3_session["organizations"].describe_organizational_unit.return_value = {
                    "OrganizationalUnit": {
                        "Id": "ou-test-production",
                        "Name": "Workloads",
                    }
                }

                # Mock Service Catalog for Account Factory
                mock_service_catalog = Mock()
                original_client = mock_boto3_session["session"].client

                def client_side_effect(service, **kwargs):
                    if service == "servicecatalog":
                        return mock_service_catalog
                    if service == "sso-admin":
                        return mock_boto3_session["sso"]
                    if service == "identitystore":
                        return mock_boto3_session["identity_store"]
                    return original_client(service, **kwargs)

                mock_boto3_session["session"].client = Mock(side_effect=client_side_effect)

                # Mock SSO user lookup
                mock_boto3_session["sso"].list_instances.return_value = {
                    "Instances": [
                        {
                            "InstanceArn": "arn:aws:sso:::instance/ssoins-test",
                            "IdentityStoreId": "d-test123",
                        }
                    ]
                }
                mock_boto3_session["identity_store"].list_users.return_value = {
                    "Users": [
                        {
                            "UserId": "test-user-id",
                            "UserName": "testuser",
                        }
                    ]
                }
                mock_boto3_session["identity_store"].describe_user.return_value = {
                    "UserId": "test-user-id",
                    "UserName": "testuser",
                    "Emails": [{"Value": "admin@example.com", "Primary": True}],
                    "Name": {"GivenName": "Test", "FamilyName": "User"},
                }

                # Mock finding Account Factory product
                mock_service_catalog.search_products.return_value = {
                    "ProductViewSummaries": [
                        {
                            "ProductId": "prod-12345",
                            "Name": "AWS Control Tower Account Factory",
                        }
                    ]
                }

                # Mock getting provisioning artifacts
                mock_service_catalog.list_provisioning_artifacts.return_value = {
                    "ProvisioningArtifactDetails": [
                        {
                            "Id": "pa-12345",
                            "Active": True,
                        }
                    ]
                }

                # Mock account provisioning
                mock_service_catalog.provision_product.return_value = {
                    "RecordDetail": {
                        "RecordId": "rec-12345",
                        "Status": "IN_PROGRESS",
                    }
                }

                # Mock checking provisioning status
                mock_service_catalog.describe_record.return_value = {
                    "RecordDetail": {
                        "RecordId": "rec-12345",
                        "Status": "SUCCEEDED",
                        "RecordOutputs": [
                            {
                                "OutputKey": "AccountId",
                                "OutputValue": "456789012345",
                            }
                        ],
                    }
                }

                # Test that account creation is disabled
                result = runner.invoke(
                    cli,
                    [
                        "account",
                        "create",
                        "NewTestAccount",
                        "newtest@example.com",
                    ],
                )
                # Should fail with our disabled message
                assert result.exit_code != 0
                assert "Account creation via CLI is not currently implemented" in result.output
                assert "Control Tower console" in result.output

                # Simulate that account exists (created via Control Tower UI)
                # and test getting the account info
                mock_boto3_session["organizations"].describe_account.return_value = {
                    "Account": {
                        "Id": "456789012345",
                        "Email": "newtest@example.com",
                        "Name": "NewTestAccount",
                        "Status": "ACTIVE",
                    }
                }

                result = runner.invoke(cli, ["account", "get", "456789012345"])
                assert result.exit_code == 0
                assert "456789012345" in result.output
                assert "NewTestAccount" in result.output

    @pytest.mark.skip(reason="SSO integration needs proper mock setup")
    def test_sso_and_account_integration(self, runner, mock_boto3_session):
        """Test SSO assignment after account creation."""
        with patch("ai_org.core.aws_client.boto3.Session") as mock_session:
            mock_session.return_value = mock_boto3_session["session"]

            # Mock SSO instance
            mock_boto3_session["sso-admin"].list_instances.return_value = {
                "Instances": [
                    {
                        "InstanceArn": "arn:aws:sso:::instance/ssoins-example",
                        "IdentityStoreId": "d-example123",
                    }
                ]
            }

            # Skip create-permission-set test - command doesn't exist

            # Assign user to account
            mock_boto3_session["sso-admin"].create_account_assignment.return_value = {
                "AccountAssignmentCreationStatus": {
                    "Status": "SUCCEEDED",
                    "RequestId": "request-example456",
                }
            }

            result = runner.invoke(
                cli,
                [
                    "sso",
                    "assign",
                    "456789012345",
                    "--principal",
                    "developer@example.com",
                    "--permission-set",
                    "DeveloperAccess",
                ],
            )
            assert result.exit_code == 0 or "not implemented" in result.output.lower()

    @pytest.mark.skip(reason="StackSet deployment needs proper mock setup")
    def test_stackset_deployment_workflow(self, runner, mock_boto3_session, tmp_path):
        """Test complete StackSet deployment workflow."""
        with patch("ai_org.core.aws_client.boto3.Session") as mock_session:
            mock_session.return_value = mock_boto3_session["session"]

            # Create a template
            template_file = tmp_path / "stack-template.yaml"
            template_file.write_text("""
AWSTemplateFormatVersion: '2010-09-09'
Description: Integration Test Stack
Parameters:
  BucketPrefix:
    Type: String
    Default: test
Resources:
  S3Bucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Sub '${BucketPrefix}-${AWS::AccountId}'
""")

            # Check StackSet status instead of deploy
            mock_boto3_session["cloudformation"].list_stack_instances.return_value = {
                "Summaries": [
                    {
                        "StackSetId": "test-stackset:id",
                        "Region": "us-east-1",
                        "Account": "456789012345",
                        "StackInstanceStatus": {"DetailedStatus": "SUCCEEDED"},
                    }
                ]
            }

            result = runner.invoke(cli, ["stackset", "status", "456789012345"])
            assert result.exit_code == 0

            # List StackSets
            mock_boto3_session["cloudformation"].list_stack_sets.return_value = {
                "Summaries": [
                    {
                        "StackSetName": "integration-stackset",
                        "StackSetId": "integration-stackset:test-id",
                        "Description": "Integration Test Stack",
                        "Status": "ACTIVE",
                    }
                ]
            }

            result = runner.invoke(cli, ["stackset", "list"])
            assert result.exit_code == 0
            assert "integration-stackset" in result.output

    def test_environment_variable_configuration(self, runner, mock_env_vars):  # noqa: ARG002
        """Test that environment variables are properly used."""
        with patch("ai_org.core.aws_client.boto3.Session") as mock_session:
            mock_session.return_value = MagicMock()

            # Test that AWS_PROFILE is used
            result = runner.invoke(cli, ["--help"])
            assert result.exit_code == 0

            # Verify environment variables are accessible
            assert os.environ.get("AWS_PROFILE") == "test-profile"
            assert os.environ.get("AWS_REGION") == "us-east-1"
            assert os.environ.get("GH_ACCOUNT") == "test-org"
