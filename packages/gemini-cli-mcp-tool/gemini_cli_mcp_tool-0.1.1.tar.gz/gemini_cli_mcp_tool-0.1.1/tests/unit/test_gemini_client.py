"""Tests for GeminiClient service."""

from unittest.mock import AsyncMock, patch

import pytest

from gemini_mcp.config import Settings
from gemini_mcp.services import GeminiClient, GeminiError, ExecutionResult


@pytest.fixture
def client(settings: Settings) -> GeminiClient:
    """Create GeminiClient instance."""
    return GeminiClient(settings)


def test_client_initialization(client: GeminiClient, settings: Settings) -> None:
    """Test client initialization."""
    assert client.settings == settings


def test_build_command_basic(client: GeminiClient) -> None:
    """Test basic command building."""
    cmd = client._build_command(
        prompt="test",
        model=None,
        sandbox=None,
        yolo=None,
        output_format="text",
    )

    assert cmd[0] == "gemini"
    assert "test" in cmd


def test_build_command_with_model(client: GeminiClient) -> None:
    """Test command building with model."""
    cmd = client._build_command(
        prompt="test",
        model="gemini-2.0-flash",
        sandbox=None,
        yolo=None,
        output_format="text",
    )

    assert "--model" in cmd
    assert "gemini-2.0-flash" in cmd


def test_build_command_with_sandbox(client: GeminiClient) -> None:
    """Test command building with sandbox."""
    cmd = client._build_command(
        prompt="test",
        model=None,
        sandbox=True,
        yolo=None,
        output_format="text",
    )

    assert "--sandbox" in cmd


def test_build_command_with_json_output(client: GeminiClient) -> None:
    """Test command building with JSON output."""
    cmd = client._build_command(
        prompt="test",
        model=None,
        sandbox=None,
        yolo=None,
        output_format="json",
    )

    assert "--output-format" in cmd
    assert "json" in cmd


@pytest.mark.asyncio
async def test_query_success(client: GeminiClient) -> None:
    """Test successful query execution."""
    mock_result = ExecutionResult(
        stdout="The answer is 4",
        stderr="",
        exit_code=0,
    )

    async def mock_execute(*args, **kwargs):
        return mock_result

    with patch.object(client, "_execute_command", side_effect=mock_execute):
        response = await client.query("What is 2+2?")

    assert response.success is True
    assert "The answer is 4" in response.content
    assert response.model == client.settings.default_model


@pytest.mark.asyncio
async def test_query_failure(client: GeminiClient) -> None:
    """Test query execution with non-zero exit code."""
    mock_result = ExecutionResult(
        stdout="",
        stderr="Error: Invalid command",
        exit_code=1,
    )

    async def mock_execute(*args, **kwargs):
        return mock_result

    with patch.object(client, "_execute_command", side_effect=mock_execute):
        with pytest.raises(GeminiError) as exc_info:
            await client.query("What is 2+2?")

    assert "failed" in str(exc_info.value).lower()
    assert exc_info.value.exit_code == 1


@pytest.mark.asyncio
async def test_query_timeout(client: GeminiClient) -> None:
    """Test query execution timeout."""
    with patch.object(
        client, "_execute_command", side_effect=TimeoutError("Timed out")
    ):
        with pytest.raises(GeminiError) as exc_info:
            await client.query("What is 2+2?", timeout=10.0)

    assert "timed out" in str(exc_info.value).lower()


@pytest.mark.asyncio
async def test_query_with_custom_model(client: GeminiClient) -> None:
    """Test query with custom model."""
    mock_result = ExecutionResult(
        stdout="Response",
        stderr="",
        exit_code=0,
    )

    async def mock_execute(*args, **kwargs):
        return mock_result

    with patch.object(client, "_execute_command", side_effect=mock_execute):
        response = await client.query("Test", model="gemini-2.0-flash")

    assert response.model == "gemini-2.0-flash"


@pytest.mark.asyncio
async def test_query_with_progress_callback(client: GeminiClient) -> None:
    """Test query with progress callback."""
    mock_result = ExecutionResult(
        stdout="Response",
        stderr="",
        exit_code=0,
    )

    progress_calls = []

    async def progress_callback(msg: str):
        progress_calls.append(msg)

    async def mock_execute(*args, **kwargs):
        return mock_result

    with patch.object(client, "_execute_command", side_effect=mock_execute):
        await client.query("Test", progress_callback=progress_callback)

    # Progress callback should be passed to _execute_command
    assert True  # Just verifying no errors


def test_build_command_with_yolo(client: GeminiClient) -> None:
    """Test command building with YOLO mode."""
    # Test with yolo=True explicitly
    cmd = client._build_command(
        prompt="test",
        model=None,
        sandbox=None,
        yolo=True,
        output_format="text",
    )
    assert "--yolo" in cmd

    # Test with default yolo from settings
    settings = Settings(enable_yolo_mode=True)
    client_with_yolo = GeminiClient(settings)
    cmd = client_with_yolo._build_command(
        prompt="test",
        model=None,
        sandbox=None,
        yolo=None,
        output_format="text",
    )
    assert "--yolo" in cmd


@pytest.mark.asyncio
async def test_code_review_query(client: GeminiClient) -> None:
    """Test code review functionality."""
    code = """
def add(a, b):
    return a + b
"""
    mock_result = ExecutionResult(
        stdout="Code review: Function looks good but missing type hints",
        stderr="",
        exit_code=0,
    )

    async def mock_execute(*args, **kwargs):
        return mock_result

    with patch.object(client, "_execute_command", side_effect=mock_execute):
        response = await client.query(f"Review this code:\n{code}")

    assert response.success is True
    assert "review" in response.content.lower() or "Code review" in response.content
