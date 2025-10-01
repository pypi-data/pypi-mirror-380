"""Command-line interface for Databricks middleware.

This module provides a CLI for testing and interacting with the Databricks
middleware Lambda functions. It includes commands for calling the middleware
and checking AWS credentials.
"""

import click

from lambda_middleware.cli.functions import call_lambda, get_caller_identity


@click.group("middleware")
def cli() -> None:
    """Databricks middleware CLI for testing Lambda functions."""
    pass


@cli.command("caller-identity")
def get_sts_caller_identity_command() -> None:
    """Display the current AWS caller identity.

    Uses AWS STS to retrieve and display information about the IAM identity
    making the request. Useful for verifying AWS credentials are configured correctly.
    """
    client_identity = get_caller_identity()
    click.echo(client_identity)


@cli.command("call")
@click.option("--message", required=True, help="Message to send to middleware")
@click.option(
    "--function-name", required=True, help="Name of the Lambda function to call"
)
def call_lambda_command(message: str, function_name: str) -> None:
    """Call the Databricks middleware Lambda function.

    Invokes the specified Lambda function with a message payload and displays
    the response. Useful for testing the middleware integration.
    """
    response = call_lambda(function_name=function_name, message=message)
    click.echo("Got the following payload from the middleware:\n")
    click.echo(response)


def main() -> None:
    """Entry point for the CLI."""
    cli()
