"""Pytest configuration and fixtures."""

import pytest

from gemini_mcp.config import Settings


@pytest.fixture
def settings() -> Settings:
    """Create test settings."""
    return Settings(
        gemini_cli_path="gemini",
        default_model="gemini-2.5-pro",
        default_timeout=120.0,
        mask_error_details=False,
        log_level="DEBUG",
    )
