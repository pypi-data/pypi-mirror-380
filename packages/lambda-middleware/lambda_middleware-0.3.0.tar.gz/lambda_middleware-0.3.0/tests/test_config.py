"""Tests for configuration management.

These tests verify expected behavior of the Config class and config loading:
- Environment variable loading
- Validation of required fields
- Config singleton behavior
"""

from unittest.mock import patch

import pytest
from pydantic import ValidationError

from lambda_middleware.config import Config, get_config


class TestConfig:
    """Tests for the Config class."""

    def test_config_with_valid_lambda_function_name(self):
        """Should successfully create config with valid lambda_function_name."""
        config = Config(lambda_function_name="my-lambda-function")

        assert config.lambda_function_name == "my-lambda-function"

    def test_config_requires_lambda_function_name(self, monkeypatch):
        """Should raise ValidationError when lambda_function_name is missing."""
        # Clear the environment variable to ensure it's not set
        monkeypatch.delenv("LAMBDA_FUNCTION_NAME", raising=False)

        # Mock _env_file to prevent loading from actual .env
        with patch.object(Config, "model_config", {"env_file": None}):
            with pytest.raises(ValidationError) as exc_info:
                Config(_env_file=None)  # type: ignore  # noqa: PGH003

            # Verify the error is about the missing field
            errors = exc_info.value.errors()
            assert len(errors) > 0
            assert any(
                error["loc"] == ("lambda_function_name",) and error["type"] == "missing"
                for error in errors
            )

    def test_config_lambda_function_name_must_be_string(self):
        """Should raise ValidationError when lambda_function_name is not a string."""
        with pytest.raises(ValidationError):
            Config(lambda_function_name=123)  # type: ignore  # noqa: PGH003

    def test_config_loads_from_env_file(self, tmp_path, monkeypatch):
        """Should load configuration from .env file."""
        # Create temporary .env file
        env_file = tmp_path / ".env"
        env_file.write_text("LAMBDA_FUNCTION_NAME=env-lambda-function\n")

        # Clear any existing env var
        monkeypatch.delenv("LAMBDA_FUNCTION_NAME", raising=False)

        # Create config with explicit env_file path
        config = Config(_env_file=str(env_file))  # type: ignore  # noqa: PGH003

        assert config.lambda_function_name == "env-lambda-function"

    def test_config_loads_from_environment_variables(self, monkeypatch):
        """Should load configuration from environment variables."""
        monkeypatch.setenv("LAMBDA_FUNCTION_NAME", "env-var-lambda-function")

        # Disable .env file loading to test only env vars
        config = Config(_env_file=None)  # type: ignore  # noqa: PGH003

        assert config.lambda_function_name == "env-var-lambda-function"

    def test_config_programmatic_overrides_env(self, monkeypatch):
        """Should prioritize programmatic config over environment variables."""
        monkeypatch.setenv("LAMBDA_FUNCTION_NAME", "env-lambda")

        config = Config(lambda_function_name="code-lambda")

        assert config.lambda_function_name == "code-lambda"

    def test_config_accepts_empty_string(self):
        """Should accept empty string as lambda_function_name (even if not useful)."""
        config = Config(lambda_function_name="")

        assert config.lambda_function_name == ""


class TestGetConfig:
    """Tests for the get_config function."""

    def test_get_config_returns_config_instance(self):
        """Should return a Config instance."""
        config = get_config()

        assert isinstance(config, Config)
        assert hasattr(config, "lambda_function_name")

    def test_get_config_returns_singleton(self):
        """Should return the same config instance on multiple calls."""
        config1 = get_config()
        config2 = get_config()

        assert config1 is config2

    def test_get_config_has_lambda_function_name(self):
        """Should have lambda_function_name attribute set."""
        config = get_config()

        # Should have the attribute, either from env or .env file
        assert isinstance(config.lambda_function_name, str)
        assert len(config.lambda_function_name) > 0
