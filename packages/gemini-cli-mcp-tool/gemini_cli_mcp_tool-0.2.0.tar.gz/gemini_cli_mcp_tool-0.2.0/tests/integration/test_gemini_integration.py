"""Integration tests for Gemini MCP tools.

These tests execute actual Gemini CLI commands to verify end-to-end functionality.
"""

import pytest

from gemini_mcp.services import GeminiClient
from gemini_mcp.config import get_settings
from gemini_mcp.tools import gemini_query, gemini_context_query


@pytest.mark.asyncio
async def test_client_simple_query():
    """Test GeminiClient with a simple query."""
    client = GeminiClient(get_settings())

    result = await client.query("What is 2+2?")

    assert result.success is True
    assert "4" in result.content
    assert result.model == "gemini-2.5-pro"


@pytest.mark.asyncio
async def test_client_with_custom_timeout():
    """Test GeminiClient with custom timeout."""
    client = GeminiClient(get_settings())

    # Quick query with short timeout
    result = await client.query("Say 'hello'", timeout=10.0)

    assert result.success is True
    assert "hello" in result.content.lower()


@pytest.mark.asyncio
async def test_tool_gemini_query():
    """Test gemini_query tool."""
    result = await gemini_query(prompt="What is 3+3?")

    assert result["success"] is True
    assert "6" in result["response"]
    assert result["model"] == "gemini-2.5-pro"


@pytest.mark.asyncio
async def test_tool_gemini_context_query():
    """Test gemini_context_query tool with context."""
    context = """
    User Profile:
    - Name: Alice
    - Age: 30
    - Location: San Francisco
    """

    result = await gemini_context_query(
        prompt="What is the user's name?",
        context=context,
    )

    assert result["success"] is True
    assert "Alice" in result["response"]
    assert result["context_size"] > 0


@pytest.mark.asyncio
async def test_tool_with_model_override():
    """Test tool with custom model (using default model since flash has API issues)."""
    # Use the default model since gemini-2.0-flash variants are having API errors
    result = await gemini_query(
        prompt="What is 5+5?",
        model="gemini-2.5-pro",
    )

    assert result["success"] is True
    assert "10" in result["response"]
    assert result["model"] == "gemini-2.5-pro"


@pytest.mark.asyncio
async def test_client_timeout_handling():
    """Test that timeout is respected."""
    client = GeminiClient(get_settings())

    # Very short timeout should fail for complex queries
    with pytest.raises(Exception) as exc_info:
        await client.query(
            "Write a 10000 word essay on quantum physics",
            timeout=0.1,
        )

    assert "timed out" in str(exc_info.value).lower()
