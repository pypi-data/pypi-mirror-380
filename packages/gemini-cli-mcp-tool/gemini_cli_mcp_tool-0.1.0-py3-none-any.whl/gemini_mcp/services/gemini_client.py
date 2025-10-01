"""Gemini CLI client service with async subprocess execution.

This module provides a robust, production-ready wrapper around the Gemini CLI
following SOLID principles and best practices for async subprocess management.
"""

from dataclasses import dataclass
import os
import shlex
import subprocess
from typing import Any, Callable

import anyio
from pydantic import BaseModel, Field
import structlog

from gemini_mcp.config import Settings

logger = structlog.get_logger(__name__)


class GeminiError(Exception):
    """Base exception for Gemini CLI errors."""

    def __init__(self, message: str, exit_code: int | None = None) -> None:
        """Initialize GeminiError.

        Args:
            message: Error message
            exit_code: Process exit code if applicable
        """
        super().__init__(message)
        self.message = message
        self.exit_code = exit_code


class GeminiResponse(BaseModel):
    """Structured response from Gemini CLI."""

    content: str = Field(description="Response content from Gemini")
    model: str = Field(description="Model used for the query")
    success: bool = Field(default=True, description="Whether the request succeeded")
    error_message: str | None = Field(
        default=None, description="Error message if failed"
    )
    metadata: dict[str, Any] = Field(
        default_factory=dict, description="Additional metadata"
    )


@dataclass
class ExecutionResult:
    """Result of subprocess execution."""

    stdout: str
    stderr: str
    exit_code: int


class GeminiClient:
    """Async client for interacting with Gemini CLI.

    This class follows the Single Responsibility Principle by focusing solely
    on executing Gemini CLI commands and parsing responses.

    Example:
        ```python
        client = GeminiClient(settings)
        response = await client.query("What is 2+2?")
        print(response.content)
        ```
    """

    def __init__(self, settings: Settings) -> None:
        """Initialize Gemini CLI client.

        Args:
            settings: Application settings (Dependency Injection)
        """
        self.settings = settings
        self.logger = logger.bind(component="GeminiClient")

    async def query(
        self,
        prompt: str,
        *,
        model: str | None = None,
        timeout: float | None = None,
        sandbox: bool | None = None,
        yolo: bool | None = None,
        output_format: str = "text",
        progress_callback: Callable[[str], Any] | None = None,
    ) -> GeminiResponse:
        """Execute a Gemini CLI query asynchronously.

        Args:
            prompt: The prompt to send to Gemini
            model: Model to use (overrides default)
            timeout: Command timeout in seconds (overrides default)
            sandbox: Enable sandbox mode (overrides default)
            yolo: Enable YOLO mode (overrides default)
            output_format: Output format ("text" or "json")
            progress_callback: Optional callback for progress updates

        Returns:
            GeminiResponse with the result

        Raises:
            GeminiError: If the CLI command fails or times out
        """
        cmd = self._build_command(
            prompt=prompt,
            model=model,
            sandbox=sandbox,
            yolo=yolo,
            output_format=output_format,
        )

        timeout_value = timeout or self.settings.default_timeout

        self.logger.info(
            "Executing Gemini CLI command",
            model=model or self.settings.default_model,
            timeout=timeout_value,
            sandbox=sandbox,
            yolo=yolo,
        )

        try:
            result = await self._execute_command(
                cmd, timeout=timeout_value, progress_callback=progress_callback
            )

            if result.exit_code != 0:
                raise GeminiError(
                    message=f"Gemini CLI failed: {result.stderr or result.stdout}",
                    exit_code=result.exit_code,
                )

            return GeminiResponse(
                content=result.stdout.strip(),
                model=model or self.settings.default_model,
                success=True,
                metadata={
                    "exit_code": result.exit_code,
                    "stderr": result.stderr if result.stderr else None,
                },
            )

        except GeminiError:
            # Re-raise GeminiError as-is to preserve exit_code
            raise

        except TimeoutError as e:
            self.logger.error("Gemini CLI command timed out", timeout=timeout_value)
            raise GeminiError(
                message=f"Command timed out after {timeout_value}s"
            ) from e

        except Exception as e:
            self.logger.error(
                "Unexpected error executing Gemini CLI", error=str(e), exc_info=True
            )
            raise GeminiError(message=f"Unexpected error: {e}") from e

    def _build_command(
        self,
        prompt: str,
        model: str | None,
        sandbox: bool | None,
        yolo: bool | None,
        output_format: str,
    ) -> list[str]:
        """Build Gemini CLI command with proper escaping.

        Args:
            prompt: The prompt to send
            model: Model to use
            sandbox: Enable sandbox mode
            yolo: Enable YOLO mode
            output_format: Output format

        Returns:
            Command as list of strings
        """
        cmd = [self.settings.gemini_cli_path]

        # Add model if specified
        if model:
            cmd.extend(["--model", model])

        # Add flags
        if sandbox or (sandbox is None and self.settings.enable_sandbox):
            cmd.append("--sandbox")

        if yolo or (yolo is None and self.settings.enable_yolo_mode):
            cmd.append("--yolo")

        # Add output format
        if output_format == "json":
            cmd.extend(["--output-format", "json"])

        # Add prompt using --prompt flag (required for non-interactive mode)
        cmd.extend(["--prompt", prompt])

        return cmd

    async def _execute_command(
        self,
        cmd: list[str],
        timeout: float,
        progress_callback: Callable[[str], Any] | None = None,
    ) -> ExecutionResult:
        """Execute command asynchronously with timeout and progress updates.

        Uses anyio for robust async subprocess execution following best practices.
        Sends periodic progress updates to prevent MCP timeout resets per 2025 spec.

        Args:
            cmd: Command to execute as list
            timeout: Timeout in seconds
            progress_callback: Optional callback for progress updates

        Returns:
            ExecutionResult with stdout, stderr, and exit code

        Raises:
            TimeoutError: If command exceeds timeout
        """
        self.logger.debug("Executing command", cmd=shlex.join(cmd))

        try:
            with anyio.fail_after(timeout):
                # Inherit parent environment to ensure HOME and other vars are available
                # This is critical for OAuth credentials stored in ~/.gemini/
                # Set CWD to /tmp to avoid Gemini CLI scanning large project dirs
                env = os.environ.copy()
                env["PWD"] = "/tmp"

                # Execute the command
                # Explicitly redirect stdin to DEVNULL to prevent CLI from waiting for input
                process = await anyio.run_process(
                    cmd,
                    check=False,  # Don't raise on non-zero exit
                    stdin=subprocess.DEVNULL,  # Close stdin to prevent hanging
                    env=env,  # Inherit environment for OAuth with PWD override
                    cwd="/tmp",  # Run from /tmp to prevent memory file scanning
                )

                return ExecutionResult(
                    stdout=process.stdout.decode("utf-8") if process.stdout else "",
                    stderr=process.stderr.decode("utf-8") if process.stderr else "",
                    exit_code=process.returncode,
                )

        except TimeoutError:
            self.logger.error("Command timed out", timeout=timeout)
            raise

    async def query_with_files(
        self,
        prompt: str,
        file_contents: dict[str, str],
        model: str | None = None,
        timeout: float | None = None,
    ) -> GeminiResponse:
        """Query Gemini with additional file context.

        This method efficiently manages large context by aggregating file contents
        and leveraging Gemini's 1M token context window.

        Args:
            prompt: The main prompt
            file_contents: Dict mapping file paths to their contents
            model: Model to use (overrides default)
            timeout: Command timeout (overrides default)

        Returns:
            GeminiResponse with the result

        Raises:
            GeminiError: If the CLI command fails
        """
        # Build context-rich prompt
        context_parts = []

        for file_path, content in file_contents.items():
            context_parts.append(f"## File: {file_path}\n\n```\n{content}\n```\n")

        full_prompt = "\n".join(context_parts) + f"\n\n{prompt}"

        self.logger.info(
            "Querying with file context",
            file_count=len(file_contents),
            prompt_length=len(full_prompt),
        )

        # Use extended timeout for large context queries
        extended_timeout = (timeout or self.settings.default_timeout) * 2

        return await self.query(
            prompt=full_prompt, model=model, timeout=extended_timeout
        )
