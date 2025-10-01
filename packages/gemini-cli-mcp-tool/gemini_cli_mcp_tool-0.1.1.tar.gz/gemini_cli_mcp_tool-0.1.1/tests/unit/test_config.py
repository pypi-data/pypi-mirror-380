"""Tests for configuration module."""

from gemini_mcp.config import Settings, get_settings


def test_settings_defaults() -> None:
    """Test default settings values."""
    settings = Settings()

    assert settings.gemini_cli_path == "gemini"
    assert settings.default_model == "gemini-2.5-pro"
    assert settings.default_timeout == 300.0  # Updated to 300s per 2025 MCP best practices
    assert settings.max_timeout == 600.0  # New max timeout setting
    assert settings.max_context_tokens == 1_000_000
    assert settings.server_name == "Gemini MCP Server"
    assert settings.mask_error_details is True
    assert settings.log_level == "INFO"


def test_settings_custom() -> None:
    """Test custom settings values."""
    settings = Settings(
        default_model="gemini-2.0-flash",
        default_timeout=60.0,
        log_level="DEBUG",
    )

    assert settings.default_model == "gemini-2.0-flash"
    assert settings.default_timeout == 60.0
    assert settings.log_level == "DEBUG"


def test_get_settings_cached() -> None:
    """Test that get_settings returns cached instance."""
    settings1 = get_settings()
    settings2 = get_settings()

    assert settings1 is settings2
