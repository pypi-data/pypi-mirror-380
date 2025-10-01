"""Configuration management for Databricks middleware client.

This module handles configuration loading from environment variables using Pydantic.
Configuration can be provided via .env files or system environment variables.
"""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """Configuration settings for Databricks middleware client.

    This class uses Pydantic to load and validate configuration from environment
    variables. Settings can be provided via a .env file or system environment variables.

    Attributes:
        lambda_function_name: Name of the AWS Lambda function that serves as the
            Databricks middleware. This is a required field.

    Environment Variables:
        LAMBDA_FUNCTION_NAME: Name of the Lambda function to invoke.

    Example:
        >>> config = Config()
        >>> print(config.lambda_function_name)
        'my-databricks-middleware'
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    lambda_function_name: str = Field(
        default=...,
        description="Name of the Databricks middleware Lambda function",
    )


config = None


def get_config() -> Config:
    """Get or create the global configuration instance.

    Returns a singleton configuration instance, creating it if it doesn't exist.
    This ensures configuration is loaded only once per application lifecycle.

    Returns:
        Global Config instance with settings loaded from environment.

    Example:
        >>> from lambda_middleware.config import get_config
        >>> config = get_config()
    """
    global config
    if not config:
        config = Config()
    return config


def reset_config() -> None:
    global config
    config = None
