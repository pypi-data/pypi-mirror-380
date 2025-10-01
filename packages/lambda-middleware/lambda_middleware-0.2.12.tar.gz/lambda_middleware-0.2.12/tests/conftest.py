"""Pytest configuration and shared fixtures for tests."""

from unittest.mock import MagicMock

import pytest

from lambda_middleware.config import Config


@pytest.fixture(autouse=True)
def set_test_env(monkeypatch):
    """Automatically set test environment variables for all tests.

    This ensures tests don't fail due to missing env vars and don't
    depend on a .env file being present. Uses autouse=True so it runs
    for every test without needing to be explicitly requested.
    """
    monkeypatch.setenv("LAMBDA_FUNCTION_NAME", "test-lambda-function")


@pytest.fixture
def mock_config() -> Config:
    """Provide a test configuration instance.

    Returns:
        Config object with test Lambda function name.
    """
    return Config(lambda_function_name="test-lambda-function")


@pytest.fixture
def mock_lambda_client() -> MagicMock:
    """Provide a mocked boto3 Lambda client.

    Returns:
        MagicMock configured to simulate Lambda client responses.
    """
    mock_client = MagicMock()

    # Configure default successful response
    mock_response = {
        "StatusCode": 200,
        "Payload": MagicMock(),
    }
    mock_response["Payload"].read.return_value = b'{"result": "success"}'
    mock_client.invoke.return_value = mock_response

    return mock_client


@pytest.fixture
def mock_sts_client() -> MagicMock:
    """Provide a mocked boto3 STS client.

    Returns:
        MagicMock configured to simulate STS client responses.
    """
    mock_client = MagicMock()
    mock_client.get_caller_identity.return_value = {
        "UserId": "AIDAI1234567890EXAMPLE",
        "Account": "123456789012",
        "Arn": "arn:aws:iam::123456789012:user/test-user",
    }
    return mock_client
