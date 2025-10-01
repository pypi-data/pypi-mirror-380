"""Middleware client for calling AWS Lambda functions that interact with Databricks API.

This module provides a simple interface to invoke Lambda functions that serve as
middleware for Databricks API operations. It handles AWS authentication, payload
formatting, and response parsing.
"""

import base64
import json

import boto3
from botocore.exceptions import ParamValidationError

from lambda_middleware.config import Config, get_config


class MiddlewareError(Exception):
    pass


class InvalidLambdaFunctionNameError(MiddlewareError):
    pass


class DatabricksMiddleware:
    """Client for calling Databricks middleware Lambda functions.

    This class provides a simple interface to invoke AWS Lambda functions that
    serve as middleware for Databricks API operations. It automatically handles
    AWS authentication via boto3, formats request payloads, and parses responses.

    Attributes:
        config: Configuration object containing Lambda function settings.
        client: boto3 Lambda client for invoking functions.

    Example:
        >>> from middleware import DatabricksMiddleware
        >>> middleware = DatabricksMiddleware()
        >>> response = await middleware.call_lambda({"query": "SELECT * FROM table"})
    """

    def __init__(self, config: Config | None = None) -> None:
        """Initialize the Databricks middleware client.

        Args:
            config: Optional configuration object. If not provided, configuration
                will be loaded from environment variables using get_config().
        """
        self.config = config if config else get_config()
        self.client = boto3.client("lambda")

    async def call_lambda(self, params: dict, dry_run: bool = False) -> dict:
        """Invoke the Databricks middleware Lambda function.

        Args:
            params: Dictionary of parameters to send to the Lambda function.
                The structure depends on the specific Lambda implementation.
            dry_run: If True, validates the request without actually invoking
                the function. Useful for testing IAM permissions. Defaults to False.

        Returns:
            Dictionary containing the Lambda function response payload. If an error
            occurs, returns a dictionary with an "error" key containing the exception.

        Example:
            >>> response = await middleware.call_lambda(
            ...     {"action": "list_clusters"},
            ...     dry_run=False
            ... )
        """

        if not self.config.lambda_function_name:
            error = "Lambda function name is not configured"
            raise InvalidLambdaFunctionNameError(error)

        payload_str = json.dumps(params)

        context = {
            "caller": "Test environment, populate with caller context",
        }
        context_json = json.dumps(context)
        context_base64 = base64.b64encode(context_json.encode("utf-8")).decode("utf-8")
        try:
            response = self.client.invoke(
                FunctionName=self.config.lambda_function_name,
                InvocationType="RequestResponse" if not dry_run else "DryRun",
                Payload=payload_str.encode("utf-8"),
                LogType="Tail",
                ClientContext=context_base64,
            )
        except ParamValidationError as e:
            return {
                "error": {"message": "Invalid paramters for Lambda call", "detail": e}
            }
        except Exception as e:
            raise e

        if "Payload" in response:
            return response["Payload"].read()
        return {
            "error": "No payload returned from lambda function",
        }
