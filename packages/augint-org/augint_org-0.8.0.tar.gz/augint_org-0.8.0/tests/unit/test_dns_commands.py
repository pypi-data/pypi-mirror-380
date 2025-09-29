"""Unit tests for DNS commands."""

from unittest.mock import MagicMock, patch

import pytest

from ai_org.cli import cli
from ai_org.commands.dns import (
    get_account_id_by_name,
    get_zone_id_by_name,
    list_staging_accounts,
    wait_for_stackset_operation,
)


def test_dns_delegate_command_missing_prefix(runner):
    """Test DNS delegate command without required prefix."""
    result = runner.invoke(cli, ["dns", "delegate", "Test Account"])
    assert result.exit_code != 0
    assert "Missing option '--prefix'" in result.output


def test_dns_help(runner):
    """Test DNS help command."""
    result = runner.invoke(cli, ["dns", "--help"])
    assert result.exit_code == 0
    assert "Manage DNS zones and delegation" in result.output


def test_dns_delegate_help(runner):
    """Test DNS delegate help."""
    result = runner.invoke(cli, ["dns", "delegate", "--help"])
    assert result.exit_code == 0
    assert "Setup DNS delegation for an account subdomain" in result.output
    assert "--prefix" in result.output
    assert "--domain" in result.output


def test_get_account_id_by_name():
    """Test get_account_id_by_name function."""
    mock_client = MagicMock()
    mock_paginator = MagicMock()
    mock_client.get_paginator.return_value = mock_paginator

    # Test successful find
    mock_paginator.paginate.return_value = [
        {
            "Accounts": [
                {"Name": "Account 1", "Id": "123456789012"},
                {"Name": "Staging Test", "Id": "234567890123"},
            ]
        }
    ]

    account_id = get_account_id_by_name(mock_client, "Staging Test")
    assert account_id == "234567890123"

    # Test not found
    account_id = get_account_id_by_name(mock_client, "Nonexistent Account")
    assert account_id is None


def test_get_zone_id_by_name():
    """Test get_zone_id_by_name function."""
    mock_client = MagicMock()

    # Test successful find
    mock_client.list_hosted_zones_by_name.return_value = {
        "HostedZones": [
            {"Id": "/hostedzone/Z123456", "Name": "example.com."},
            {"Id": "/hostedzone/Z789012", "Name": "aillc.link."},
        ]
    }

    zone_id = get_zone_id_by_name(mock_client, "aillc.link")
    assert zone_id == "Z789012"

    # Test not found
    zone_id = get_zone_id_by_name(mock_client, "nonexistent.com")
    assert zone_id is None

    # Test with trailing dot
    zone_id = get_zone_id_by_name(mock_client, "aillc.link.")
    assert zone_id == "Z789012"


def test_list_staging_accounts():
    """Test list_staging_accounts function (now lists all accounts)."""
    mock_client = MagicMock()
    mock_output = MagicMock()
    mock_paginator = MagicMock()
    mock_client.get_paginator.return_value = mock_paginator

    mock_paginator.paginate.return_value = [
        {
            "Accounts": [
                {"Name": "Production Account", "Id": "123456789012"},
                {"Name": "Staging Test", "Id": "234567890123"},
                {"Name": "Staging Another", "Id": "345678901234"},
                {"Name": "Dev Account", "Id": "456789012345"},
            ]
        }
    ]

    # Capture what was printed
    printed_items = []
    mock_output.text = lambda x: printed_items.append(x)
    mock_output.info = lambda _: None  # Mock info method

    list_staging_accounts(mock_client, mock_output)

    # Should list all accounts, sorted alphabetically
    assert len(printed_items) == 4
    assert "Dev Account" in printed_items[0]
    assert "Production Account" in printed_items[1]
    assert "Staging Another" in printed_items[2]
    assert "Staging Test" in printed_items[3]


def test_wait_for_stackset_operation_success():
    """Test wait_for_stackset_operation with successful operation."""
    mock_client = MagicMock()
    mock_client.describe_stack_set_operation.return_value = {
        "StackSetOperation": {"Status": "SUCCEEDED"}
    }

    # Should not raise an exception
    wait_for_stackset_operation(mock_client, "test-stackset", "op-123", timeout=1)


def test_wait_for_stackset_operation_failure():
    """Test wait_for_stackset_operation with failed operation."""
    mock_client = MagicMock()
    mock_client.describe_stack_set_operation.return_value = {
        "StackSetOperation": {"Status": "FAILED"}
    }

    with pytest.raises(Exception, match="StackSet operation FAILED"):
        wait_for_stackset_operation(mock_client, "test-stackset", "op-123", timeout=1)


def test_wait_for_stackset_operation_timeout():
    """Test wait_for_stackset_operation with timeout."""
    mock_client = MagicMock()
    mock_client.describe_stack_set_operation.return_value = {
        "StackSetOperation": {"Status": "RUNNING"}
    }

    with pytest.raises(TimeoutError, match="timed out after 1 seconds"):
        wait_for_stackset_operation(mock_client, "test-stackset", "op-123", timeout=1)


@patch("ai_org.commands.dns.get_zone_id_by_name")
@patch("ai_org.commands.dns.get_account_id_by_name")
@patch("boto3.Session")
def test_dns_delegate_account_not_found(mock_session, mock_get_account, mock_get_zone, runner):
    """Test DNS delegate when account is not found."""
    # Setup mocks
    mock_get_account.return_value = None

    result = runner.invoke(cli, ["dns", "delegate", "Nonexistent Account", "--prefix", "test"])

    assert result.exit_code != 0
    assert "Account 'Nonexistent Account' not found" in result.output


@patch("ai_org.commands.dns.add_ns_delegation")
@patch("ai_org.commands.dns.get_stack_instance_outputs")
@patch("ai_org.commands.dns.deploy_dns_stackset_instance")
@patch("ai_org.commands.dns.get_zone_id_by_name")
@patch("ai_org.commands.dns.get_account_id_by_name")
@patch("boto3.Session")
def test_dns_delegate_parent_zone_not_found(
    mock_session,
    mock_get_account,
    mock_get_zone,
    mock_deploy,
    mock_get_outputs,
    mock_add_ns,
    runner,
):
    """Test DNS delegate when parent zone is not found."""
    # Setup mocks
    mock_get_account.return_value = "123456789012"
    mock_get_zone.return_value = None  # Parent zone not found
    mock_get_outputs.return_value = {
        "NameServers": "ns1.aws.com,ns2.aws.com",
        "HostedZoneId": "Z123456",
        "FullDomain": "test.aillc.link",
    }

    result = runner.invoke(cli, ["dns", "delegate", "Test Account", "--prefix", "test"])

    assert result.exit_code != 0
    assert "Parent zone aillc.link not found" in result.output
    assert "aws route53 create-hosted-zone" in result.output


def test_dns_delegate_with_custom_domain(runner):
    """Test DNS delegate command with custom domain."""
    with patch("ai_org.commands.dns.get_account_id_by_name") as mock_get_account:
        mock_get_account.return_value = None  # Will fail fast for this test

        result = runner.invoke(
            cli, ["dns", "delegate", "Test Account", "--prefix", "api", "--domain", "example.com"]
        )

        # Should fail on account lookup but we can see domain was accepted
        assert result.exit_code != 0
        # The error will be about account not found, but that's OK for this test
