"""Helper functions for the CLI commands.

This module contains business logic for CLI commands, separated from the
Click command definitions for better testability.
"""

import asyncio
from typing import Any

import boto3

from lambda_middleware.config import get_config
from lambda_middleware.middleware import LambdaMiddleware


def get_caller_identity() -> dict[str, Any]:
    """Get the AWS caller identity using STS.

    Uses boto3 STS client to retrieve information about the IAM identity
    making the request. Useful for verifying AWS credentials.

    Returns:
        Dictionary containing UserId, Account, and Arn of the caller.

    Example:
        >>> identity = get_caller_identity()
        >>> print(identity["Account"])
        '123456789012'
    """
    client = boto3.client("sts")
    return client.get_caller_identity()


def call_lambda(function_name: str, message: str) -> dict[str, Any]:
    """Call the Databricks middleware Lambda function with a message.

    Creates a middleware client configured for the specified Lambda function
    and invokes it with the provided message payload.

    Args:
        function_name: Name of the AWS Lambda function to invoke.
        message: Message string to send as the payload.

    Returns:
        Dictionary containing the Lambda function response.

    Example:
        >>> response = call_lambda("my-lambda", "test message")
    """
    config = get_config()
    config.lambda_function_name = function_name
    middleware = LambdaMiddleware(config=config)

    return asyncio.run(
        middleware.call_lambda(
            {
                "message": message,
            }
        )
    )
