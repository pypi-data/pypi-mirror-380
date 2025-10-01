"""Tests for CLI commands.

These tests verify expected behavior of CLI commands:
- caller-identity command shows AWS identity
- call command invokes Lambda with correct parameters
- Proper error handling and output formatting
"""

from unittest.mock import MagicMock, patch

import pytest
from click.testing import CliRunner

from lambda_middleware.cli.main import cli


class TestCallerIdentityCommand:
    """Tests for the caller-identity CLI command."""

    def test_caller_identity_displays_aws_identity(self, mock_sts_client):
        """Should display AWS caller identity information."""
        runner = CliRunner()

        with patch(
            "lambda_middleware.cli.functions.boto3.client", return_value=mock_sts_client
        ):
            result = runner.invoke(cli, ["caller-identity"])

            assert result.exit_code == 0
            assert "AIDAI1234567890EXAMPLE" in result.output
            assert "123456789012" in result.output
            assert "arn:aws:iam::123456789012:user/test-user" in result.output

    def test_caller_identity_handles_aws_error(self):
        """Should handle AWS errors gracefully."""
        runner = CliRunner()
        mock_client = MagicMock()
        mock_client.get_caller_identity.side_effect = Exception("AWS Error")

        with patch(
            "lambda_middleware.cli.functions.boto3.client", return_value=mock_client
        ):
            result = runner.invoke(cli, ["caller-identity"])

            # Command should fail with non-zero exit code
            assert result.exit_code != 0

    def test_caller_identity_command_name(self):
        """Should be accessible via 'caller-identity' command."""
        runner = CliRunner()

        # Test that the command exists
        result = runner.invoke(cli, ["caller-identity", "--help"])

        assert result.exit_code == 0
        assert "caller-identity" in result.output.lower()


class TestCallCommand:
    """Tests for the call CLI command."""

    def test_call_invokes_lambda_with_message(self, mock_lambda_client):
        """Should invoke Lambda function with provided message."""
        runner = CliRunner()

        with patch(
            "lambda_middleware.middleware.boto3.client", return_value=mock_lambda_client
        ):
            with patch("lambda_middleware.cli.functions.get_config") as mock_get_config:
                mock_config = MagicMock()
                mock_get_config.return_value = mock_config

                result = runner.invoke(
                    cli,
                    [
                        "call",
                        "--function-name",
                        "test-lambda",
                        "--message",
                        "test message",
                    ],
                )

                assert result.exit_code == 0
                assert "Got the following payload from the middleware" in result.output
                mock_config.lambda_function_name = "test-lambda"

    def test_call_requires_function_name(self):
        """Should handle missing --function-name option."""
        runner = CliRunner()

        result = runner.invoke(cli, ["call", "--message", "test"])

        # Should fail without function name
        assert result.exit_code != 0

    def test_call_requires_message(self):
        """Should handle missing --message option."""
        runner = CliRunner()

        result = runner.invoke(cli, ["call", "--function-name", "test-lambda"])

        # Should fail without message
        assert result.exit_code != 0

    def test_call_displays_response_payload(self, mock_lambda_client):
        """Should display the Lambda response payload."""
        runner = CliRunner()

        with patch(
            "lambda_middleware.middleware.boto3.client", return_value=mock_lambda_client
        ):
            with patch("lambda_middleware.cli.functions.get_config") as mock_get_config:
                mock_get_config.return_value = MagicMock()

                result = runner.invoke(
                    cli,
                    [
                        "call",
                        "--function-name",
                        "test-lambda",
                        "--message",
                        "test",
                    ],
                )

                assert result.exit_code == 0
                assert "payload" in result.output.lower()

    def test_call_command_name(self):
        """Should be accessible via 'call' command."""
        runner = CliRunner()

        result = runner.invoke(cli, ["call", "--help"])

        assert result.exit_code == 0
        assert "--message" in result.output
        assert "--function-name" in result.output


class TestCliGroup:
    """Tests for the main CLI group."""

    def test_cli_group_exists(self):
        """Should have a CLI group named 'middleware'."""
        runner = CliRunner()

        result = runner.invoke(cli, ["--help"])

        assert result.exit_code == 0
        assert "middleware" in result.output.lower()

    def test_cli_shows_available_commands(self):
        """Should list available commands in help output."""
        runner = CliRunner()

        result = runner.invoke(cli, ["--help"])

        assert result.exit_code == 0
        assert "caller-identity" in result.output
        assert "call" in result.output

    def test_cli_handles_unknown_command(self):
        """Should handle unknown commands gracefully."""
        runner = CliRunner()

        result = runner.invoke(cli, ["unknown-command"])

        assert result.exit_code != 0
        assert "Error" in result.output or "No such command" in result.output


class TestCliIntegration:
    """Integration tests for CLI functionality."""

    @pytest.mark.asyncio
    async def test_call_command_uses_asyncio(self, mock_lambda_client):
        """Should properly use asyncio to run async middleware call."""
        runner = CliRunner()

        with patch(
            "lambda_middleware.middleware.boto3.client", return_value=mock_lambda_client
        ):
            with patch("lambda_middleware.cli.functions.get_config") as mock_get_config:
                with patch(
                    "lambda_middleware.cli.functions.asyncio.run"
                ) as mock_asyncio_run:
                    mock_get_config.return_value = MagicMock()
                    mock_asyncio_run.return_value = {"result": "success"}

                    result = runner.invoke(
                        cli,
                        [
                            "call",
                            "--function-name",
                            "test-lambda",
                            "--message",
                            "test",
                        ],
                    )

                    # Verify asyncio.run was called
                    mock_asyncio_run.assert_called_once()
                    assert result.exit_code == 0
