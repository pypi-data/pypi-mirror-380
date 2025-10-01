# Factored Databricks Middleware

A Python client library for calling AWS Lambda functions that serve as middleware to the Databricks API. This package simplifies the integration with your organization's Databricks infrastructure by providing a clean, typed interface for Lambda invocations.

## Features

- **Simple API**: Just instantiate `DatabricksMiddleware` and call methods
- **Flexible Configuration**: Environment variables or programmatic configuration
- **CLI Interface**: Test Lambda functions from the command line
- **Type Safe**: Full type hints with Pydantic validation
- **AWS Integration**: Built on boto3 for seamless AWS authentication

## Installation

Install via pip or uv:

```bash
pip install lambda-middleware
# OR
uv add lambda-middleware
```

## Configuration

Set the Lambda function name via environment variable:

```bash
export LAMBDA_FUNCTION_NAME=your-databricks-middleware-function
```

Or create a `.env` file:

```env
LAMBDA_FUNCTION_NAME=your-databricks-middleware-function
```

## Usage

### Programmatic Usage

```python
import asyncio
from lambda_middleware import DatabricksMiddleware

# Initialize with environment config
middleware = DatabricksMiddleware()

# Or provide custom config
from middleware.config import Config
config = Config(lambda_function_name="my-function")
middleware = DatabricksMiddleware(config=config)

# Call the Lambda function
async def main():
    response = await middleware.call_lambda({
        "action": "list_clusters",
        "params": {}
    })
    print(response)

asyncio.run(main())
```

### CLI Usage

Check AWS credentials:

```bash
middleware caller-identity
```

Call the Lambda function:

```bash
middleware call --function-name my-databricks-middleware --message "test payload"
```

### Dry Run Mode

Test IAM permissions without invoking the function:

```python
response = await middleware.call_lambda(
    {"action": "describe_cluster"},
    dry_run=True
)
```

## Requirements

- Python 3.13+
- AWS credentials configured (via `~/.aws/credentials`, environment variables, or IAM role)
- Access to the target Lambda function

## Development

Install development dependencies:

```bash
uv add --dev pytest pytest-mock pytest-asyncio
```

Run tests:

```bash
pytest
```

## License

Internal use only - Factored organization.