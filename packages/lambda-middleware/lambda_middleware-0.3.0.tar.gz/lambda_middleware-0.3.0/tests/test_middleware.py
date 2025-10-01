"""Tests for the DatabricksMiddleware class.

These tests verify expected behavior of the middleware client, including:
- Proper initialization with and without config
- Successful Lambda invocations
- Error handling
- Dry run mode functionality
"""

import json
from unittest.mock import MagicMock, patch

import pytest

from lambda_middleware.config import Config
from lambda_middleware.middleware import DatabricksMiddleware


class TestDatabricksMiddlewareInit:
    """Tests for DatabricksMiddleware initialization."""

    def test_init_with_config(self, mock_config):
        """Should initialize with provided config."""
        with patch("lambda_middleware.middleware.boto3.client") as mock_boto_client:
            middleware = DatabricksMiddleware(config=mock_config)

            assert middleware.config == mock_config
            assert middleware.config.lambda_function_name == "test-lambda-function"
            mock_boto_client.assert_called_once_with("lambda")

    def test_init_without_config(self):
        """Should initialize with config from environment when not provided."""
        with patch("lambda_middleware.middleware.get_config") as mock_get_config:
            with patch("lambda_middleware.middleware.boto3.client"):
                mock_config = Config(lambda_function_name="env-lambda-function")
                mock_get_config.return_value = mock_config

                middleware = DatabricksMiddleware()

                assert middleware.config == mock_config
                mock_get_config.assert_called_once()

    def test_creates_lambda_client(self, mock_config):
        """Should create a boto3 Lambda client on initialization."""
        with patch("lambda_middleware.middleware.boto3.client") as mock_boto_client:
            mock_client = MagicMock()
            mock_boto_client.return_value = mock_client

            middleware = DatabricksMiddleware(config=mock_config)

            assert middleware.client == mock_client


class TestDatabricksMiddlewareCallLambda:
    """Tests for the call_lambda method."""

    @pytest.mark.asyncio
    async def test_successful_lambda_invocation(self, mock_config, mock_lambda_client):
        """Should successfully invoke Lambda and return payload."""
        with patch(
            "lambda_middleware.middleware.boto3.client", return_value=mock_lambda_client
        ):
            middleware = DatabricksMiddleware(config=mock_config)
            params = {"action": "list_clusters", "workspace_id": "123"}

            response = await middleware.call_lambda(params)

            # Verify Lambda was called with correct parameters
            mock_lambda_client.invoke.assert_called_once()
            call_args = mock_lambda_client.invoke.call_args

            assert call_args.kwargs["FunctionName"] == "test-lambda-function"
            assert call_args.kwargs["InvocationType"] == "RequestResponse"
            assert call_args.kwargs["LogType"] == "Tail"

            # Verify payload was correctly formatted
            payload = json.loads(call_args.kwargs["Payload"].decode("utf-8"))
            assert payload == params

            # Verify response
            assert response == b'{"result": "success"}'

    @pytest.mark.asyncio
    async def test_lambda_invocation_with_dry_run(
        self, mock_config, mock_lambda_client
    ):
        """Should use DryRun invocation type when dry_run is True."""
        with patch(
            "lambda_middleware.middleware.boto3.client", return_value=mock_lambda_client
        ):
            middleware = DatabricksMiddleware(config=mock_config)
            params = {"action": "test_action"}

            await middleware.call_lambda(params, dry_run=True)

            call_args = mock_lambda_client.invoke.call_args
            assert call_args.kwargs["InvocationType"] == "DryRun"

    @pytest.mark.asyncio
    async def test_lambda_invocation_includes_client_context(
        self, mock_config, mock_lambda_client
    ):
        """Should include base64-encoded client context in Lambda invocation."""
        with patch(
            "lambda_middleware.middleware.boto3.client", return_value=mock_lambda_client
        ):
            middleware = DatabricksMiddleware(config=mock_config)
            params = {"action": "test"}

            await middleware.call_lambda(params)

            call_args = mock_lambda_client.invoke.call_args
            assert "ClientContext" in call_args.kwargs
            # ClientContext should be base64-encoded JSON
            assert isinstance(call_args.kwargs["ClientContext"], str)

    @pytest.mark.asyncio
    async def test_lambda_invocation_propagates_exception(self, mock_config):
        """Should propagate exception when Lambda invocation fails."""
        mock_client = MagicMock()
        exception = Exception("Lambda invocation failed")
        mock_client.invoke.side_effect = exception

        with patch(
            "lambda_middleware.middleware.boto3.client", return_value=mock_client
        ):
            middleware = DatabricksMiddleware(config=mock_config)

            with pytest.raises(Exception) as exc_info:
                await middleware.call_lambda({"action": "test"})

            assert str(exc_info.value) == "Lambda invocation failed"

    @pytest.mark.asyncio
    async def test_lambda_response_without_payload(self, mock_config):
        """Should return error when Lambda response has no Payload."""
        mock_client = MagicMock()
        # Response without Payload key
        mock_client.invoke.return_value = {"StatusCode": 200}

        with patch(
            "lambda_middleware.middleware.boto3.client", return_value=mock_client
        ):
            middleware = DatabricksMiddleware(config=mock_config)

            response = await middleware.call_lambda({"action": "test"})

            assert "error" in response
            assert response["error"] == "No payload returned from lambda function"

    @pytest.mark.asyncio
    async def test_lambda_invocation_with_empty_params(
        self, mock_config, mock_lambda_client
    ):
        """Should handle empty params dict correctly."""
        with patch(
            "lambda_middleware.middleware.boto3.client", return_value=mock_lambda_client
        ):
            middleware = DatabricksMiddleware(config=mock_config)

            await middleware.call_lambda({})

            mock_lambda_client.invoke.assert_called_once()
            call_args = mock_lambda_client.invoke.call_args
            payload = json.loads(call_args.kwargs["Payload"].decode("utf-8"))
            assert payload == {}

    @pytest.mark.asyncio
    async def test_lambda_invocation_with_complex_params(
        self, mock_config, mock_lambda_client
    ):
        """Should correctly serialize complex nested params."""
        with patch(
            "lambda_middleware.middleware.boto3.client", return_value=mock_lambda_client
        ):
            middleware = DatabricksMiddleware(config=mock_config)
            complex_params = {
                "action": "create_cluster",
                "config": {
                    "cluster_name": "test-cluster",
                    "spark_version": "11.3.x-scala2.12",
                    "node_type_id": "i3.xlarge",
                    "num_workers": 2,
                    "tags": {"environment": "dev", "team": "data"},
                },
            }

            await middleware.call_lambda(complex_params)

            call_args = mock_lambda_client.invoke.call_args
            payload = json.loads(call_args.kwargs["Payload"].decode("utf-8"))
            assert payload == complex_params
