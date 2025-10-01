"""Settings configuration using Pydantic Settings."""

from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings with environment variable support."""

    model_config = SettingsConfigDict(
        env_prefix="GEMINI_MCP_",
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Gemini CLI Configuration
    gemini_cli_path: str = Field(
        default="gemini",
        description="Path to Gemini CLI executable",
    )

    default_model: str = Field(
        default="gemini-2.5-pro",
        description="Default Gemini model to use",
    )

    # Execution Configuration
    default_timeout: float = Field(
        default=300.0,
        description="Default timeout for Gemini CLI commands (seconds)",
        gt=0,
    )

    max_timeout: float = Field(
        default=600.0,
        description="Maximum allowed timeout for any operation (seconds)",
        gt=0,
    )

    max_context_tokens: int = Field(
        default=1_000_000,
        description="Maximum context window size in tokens",
        gt=0,
    )

    # Server Configuration
    server_name: str = Field(
        default="Gemini MCP Server",
        description="MCP server name",
    )

    mask_error_details: bool = Field(
        default=True,
        description="Mask internal error details in production",
    )

    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = Field(
        default="INFO",
        description="Logging level",
    )

    # Feature Flags
    enable_sandbox: bool = Field(
        default=False,
        description="Enable sandbox mode by default",
    )

    enable_yolo_mode: bool = Field(
        default=False,
        description="Enable YOLO mode (auto-approve) by default",
    )


@lru_cache
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
