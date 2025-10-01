#!/usr/bin/env python3
"""Smoke test to verify lambda-middleware package is working correctly.

This script tests that the package can be imported and basic functionality works.
If anything fails, the script will exit with an error showing what broke.
"""

import importlib.metadata
import subprocess
from unittest.mock import MagicMock, patch

# Test 1: Import all modules
print("🔍 Testing imports...")
from lambda_middleware.cli.main import cli  # noqa: E402, F401
from lambda_middleware.config import Config, get_config  # noqa: E402, F401
from lambda_middleware.middleware import DatabricksMiddleware  # noqa: E402

print("✅ All imports successful\n")

# Test 2: Create config
print("🔍 Testing Config creation...")
config = Config(lambda_function_name="test-function")
assert config.lambda_function_name == "test-function"
print("✅ Config creation works\n")

# Test 3: Instantiate middleware (with mocked boto3)
print("🔍 Testing DatabricksMiddleware instantiation...")
with patch("lambda_middleware.middleware.boto3.client") as mock_boto:
    mock_boto.return_value = MagicMock()
    middleware = DatabricksMiddleware(config=config)
    assert middleware.config.lambda_function_name == "test-function"
    assert middleware.client is not None
print("✅ Middleware instantiation works\n")

# Test 4: CLI is available
print("🔍 Testing CLI availability...")
result = subprocess.run(
    ["lambda-middleware", "--help"], capture_output=True, text=True, timeout=5
)
assert result.returncode == 0, f"CLI failed with: {result.stderr}"
assert "Databricks middleware CLI" in result.stdout
print("✅ CLI is available and working\n")

# Test 5: Package metadata
print("🔍 Testing package metadata...")
metadata = importlib.metadata.metadata("lambda-middleware")
version = importlib.metadata.version("lambda-middleware")
print(f"   Package: {metadata['Name']}")
print(f"   Version: {version}")
print(f"   Summary: {metadata['Summary']}")
assert metadata["Name"] == "lambda-middleware"
assert version is not None
print("✅ Package metadata is correct\n")

print("=" * 60)
print("✅ All smoke tests passed!")
print("=" * 60)
