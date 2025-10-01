"""Gemini MCP tools implementation.

This module implements MCP tools for interacting with Gemini CLI,
following SOLID principles and FastMCP best practices.
"""

from typing import Annotated

from fastmcp import Context
from fastmcp.exceptions import ToolError
from pydantic import Field
import structlog

from gemini_mcp.config import get_settings
from gemini_mcp.services import GeminiClient, GeminiError

logger = structlog.get_logger(__name__)


async def gemini_query(
    prompt: Annotated[
        str,
        Field(description="The prompt to send to Gemini", min_length=1),
    ],
    model: Annotated[
        str | None,
        Field(
            description="Model to use (e.g., 'gemini-2.5-pro', 'gemini-2.0-flash')",
            examples=["gemini-2.5-pro", "gemini-2.0-flash"],
        ),
    ] = None,
    timeout: Annotated[
        float | None,
        Field(
            description="Timeout in seconds (default: 300, max: 600)",
            gt=0,
            le=600,
        ),
    ] = None,
    sandbox: Annotated[
        bool,
        Field(
            description="Enable sandbox mode for isolated execution",
        ),
    ] = False,
    ctx: Context | None = None,
) -> dict[str, str | bool]:
    """Query Gemini CLI with a prompt.

    This tool provides direct access to Gemini's powerful language models,
    enabling AI assistants to leverage Gemini's large context window (1M tokens)
    and free tier for token-efficient operations.

    Args:
        prompt: The question or instruction to send to Gemini
        model: Optional model override (defaults to gemini-2.5-pro)
        timeout: Optional timeout in seconds (defaults to 120s)
        sandbox: Enable sandbox mode for code execution
        ctx: FastMCP context for logging

    Returns:
        Dict containing:
            - response: The text response from Gemini
            - model: The model used
            - success: Whether the query succeeded

    Raises:
        ToolError: If the Gemini CLI command fails

    Example:
        ```python
        result = await gemini_query(
            prompt="Explain quantum computing in simple terms",
            model="gemini-2.5-pro"
        )
        print(result["response"])
        ```
    """
    settings = get_settings()
    client = GeminiClient(settings)

    if ctx:
        await ctx.info(
            f"Querying Gemini with model: {model or settings.default_model}"
        )
        await ctx.debug(f"Prompt: {prompt[:100]}...")

    try:
        if ctx:
            await ctx.report_progress(0, 1, "Sending query to Gemini...")

        # Create progress callback to keep connection alive during long operations
        async def progress_callback(message: str):
            if ctx:
                await ctx.report_progress(0, 1, message)

        response = await client.query(
            prompt=prompt,
            model=model,
            timeout=timeout,
            sandbox=sandbox,
            progress_callback=progress_callback if ctx else None,
        )

        if ctx:
            await ctx.report_progress(1, 1, "Query completed")
            await ctx.info(
                f"Received response: {len(response.content)} characters"
            )

        return {
            "response": response.content,
            "model": response.model,
            "success": response.success,
        }

    except GeminiError as e:
        if ctx:
            await ctx.error(f"Gemini query failed: {e.message}")
        # Use ToolError to ensure message is sent to client
        raise ToolError(f"Gemini query failed: {e.message}") from e


async def gemini_context_query(
    prompt: Annotated[
        str,
        Field(description="The main question or instruction", min_length=1),
    ],
    context: Annotated[
        str,
        Field(
            description=(
                "Additional context or content to include "
                "(e.g., file contents, documentation)"
            ),
            min_length=1,
        ),
    ],
    model: Annotated[
        str | None,
        Field(description="Model to use (defaults to gemini-2.5-pro)"),
    ] = None,
    timeout: Annotated[
        float | None,
        Field(description="Timeout in seconds (default: 240 for large context)", gt=0),
    ] = None,
    ctx: Context | None = None,
) -> dict[str, str | bool | int]:
    """Query Gemini with large context content.

    This tool is optimized for queries that require substantial context,
    such as analyzing large codebases, documents, or datasets.
    Leverages Gemini's 1M token context window efficiently.

    Args:
        prompt: The main question or instruction
        context: Additional context to provide (file contents, docs, etc.)
        model: Optional model override
        timeout: Optional timeout (default: 240s for large contexts)
        ctx: FastMCP context for logging

    Returns:
        Dict containing:
            - response: The text response from Gemini
            - model: The model used
            - success: Whether the query succeeded
            - context_size: Size of context provided in characters

    Raises:
        ToolError: If the Gemini CLI command fails

    Example:
        ```python
        result = await gemini_context_query(
            prompt="Find all security vulnerabilities",
            context=large_codebase_content
        )
        ```
    """
    settings = get_settings()
    client = GeminiClient(settings)

    if ctx:
        await ctx.info(f"Processing query with {len(context)} chars of context")

    # Build context-rich prompt
    full_prompt = f"""# Context

{context}

# Question

{prompt}
"""

    try:
        if ctx:
            await ctx.report_progress(0, 1, "Sending query with context to Gemini...")

        # Create progress callback to keep connection alive during long operations
        async def progress_callback(message: str):
            if ctx:
                await ctx.report_progress(0, 1, message)

        # Use extended timeout for large context
        query_timeout = timeout or (settings.default_timeout * 2)

        response = await client.query(
            prompt=full_prompt,
            model=model,
            timeout=query_timeout,
            progress_callback=progress_callback if ctx else None,
        )

        if ctx:
            await ctx.report_progress(1, 1, "Query completed")
            await ctx.info("Context query completed successfully")

        return {
            "response": response.content,
            "model": response.model,
            "success": response.success,
            "context_size": len(context),
        }

    except GeminiError as e:
        if ctx:
            await ctx.error(f"Context query failed: {e.message}")
        raise ToolError(f"Context query failed: {e.message}") from e


async def gemini_analyze_codebase(
    prompt: Annotated[
        str,
        Field(
            description=(
                "Analysis question or instruction "
                "(e.g., 'Find security issues', 'Explain architecture')"
            ),
            min_length=1,
        ),
    ],
    codebase_content: Annotated[
        str,
        Field(
            description=(
                "The codebase content to analyze (file contents, directory structure, etc.)"
            ),
            min_length=1,
        ),
    ],
    model: Annotated[
        str | None,
        Field(description="Model to use (defaults to gemini-2.5-pro)"),
    ] = None,
    ctx: Context | None = None,
) -> dict[str, str | bool]:
    """Analyze a codebase using Gemini's large context window.

    This tool leverages Gemini's 1M token context window to perform
    comprehensive codebase analysis without requiring external tools.

    Args:
        prompt: The analysis question or instruction
        codebase_content: The codebase content to analyze
        model: Optional model override
        ctx: FastMCP context for logging

    Returns:
        Dict containing:
            - analysis: The analysis result from Gemini
            - model: The model used
            - success: Whether the analysis succeeded

    Raises:
        ToolError: If Gemini CLI fails

    Example:
        ```python
        result = await gemini_analyze_codebase(
            prompt="Analyze the security of this codebase",
            codebase_content=codebase_digest
        )
        ```
    """
    settings = get_settings()
    client = GeminiClient(settings)

    if ctx:
        await ctx.info(f"Analyzing codebase: {len(codebase_content)} characters")
        await ctx.report_progress(0, 2, "Preparing analysis...")

    try:
        # Build analysis prompt
        analysis_prompt = (
            f"# Codebase Analysis Request\n\n"
            f"{prompt}\n\n"
            f"# Repository Contents\n\n"
            f"{codebase_content}\n"
        )

        if ctx:
            await ctx.report_progress(1, 2, "Analyzing with Gemini...")

        # Create progress callback to keep connection alive during long operations
        async def progress_callback(message: str):
            if ctx:
                await ctx.report_progress(1, 2, message)

        # Use extended timeout for large context
        response = await client.query(
            prompt=analysis_prompt,
            model=model,
            timeout=settings.default_timeout * 3,
            progress_callback=progress_callback if ctx else None,
        )

        if ctx:
            await ctx.report_progress(2, 2, "Analysis complete")
            await ctx.info("Codebase analysis completed successfully")

        return {
            "analysis": response.content,
            "model": response.model,
            "success": response.success,
        }

    except GeminiError as e:
        if ctx:
            await ctx.error(f"Gemini analysis failed: {e.message}")
        raise ToolError(f"Analysis failed: {e.message}") from e


async def gemini_code_review(
    code: Annotated[
        str,
        Field(
            description="The code to review (can be a single file, diff, or PR content)",
            min_length=1,
        ),
    ],
    context: Annotated[
        str | None,
        Field(
            description="Optional context about the code (e.g., project description, related files)",
        ),
    ] = None,
    review_focus: Annotated[
        str | None,
        Field(
            description=(
                "Specific areas to focus on "
                "(e.g., 'security', 'performance', 'logic errors', 'all')"
            ),
        ),
    ] = None,
    model: Annotated[
        str | None,
        Field(description="Model to use (defaults to gemini-2.5-pro)"),
    ] = None,
    ctx: Context | None = None,
) -> dict[str, str | bool]:
    """Review code using Gemini's adversarial critic capabilities.

    This tool acts as an adversarial code reviewer, identifying:
    - Subtle logic errors
    - Inefficient algorithms
    - Security vulnerabilities
    - Edge cases and potential bugs
    - Code quality issues
    - Best practice violations

    The review goes beyond simple linting to understand code intent and context.

    Args:
        code: The code to review
        context: Optional additional context about the code
        review_focus: Specific areas to focus review on (default: comprehensive)
        model: Optional model override
        ctx: FastMCP context for logging

    Returns:
        Dict containing:
            - review: The detailed code review from Gemini
            - model: The model used
            - success: Whether the review succeeded

    Raises:
        ToolError: If Gemini CLI fails

    Example:
        ```python
        result = await gemini_code_review(
            code=file_contents,
            review_focus="security and logic errors"
        )
        print(result["review"])
        ```
    """
    settings = get_settings()
    client = GeminiClient(settings)

    if ctx:
        await ctx.info(f"Starting code review: {len(code)} characters")
        await ctx.report_progress(0, 1, "Analyzing code...")

    try:
        # Build comprehensive adversarial review prompt
        review_prompt = f"""You are an expert code reviewer acting as a critic. Your role is to provide thorough adversarial review of code.

# Review Guidelines

Identify and report:
1. **Logic Errors**: Subtle bugs, off-by-one errors, incorrect algorithms
2. **Edge Cases**: Inputs that might break the code
3. **Performance Issues**: Inefficient algorithms (e.g., unnecessary O(n²) complexity)
4. **Security Vulnerabilities**: SQL injection, XSS, insecure patterns
5. **Code Quality**: Readability, maintainability, best practices
6. **API/Interface Issues**: Signature mismatches, missing parameters
7. **Testing Gaps**: Areas that need better test coverage

# Code to Review

```
{code}
```
"""

        if context:
            review_prompt += f"""
# Additional Context

{context}
"""

        if review_focus:
            review_prompt += f"""
# Review Focus

Pay special attention to: {review_focus}
"""

        review_prompt += """
# Output Format

Provide your review in the following structure:

## Summary
Brief overview of code quality and main concerns

## Critical Issues
Issues that must be fixed (security, logic errors, bugs)

## Performance Concerns
Algorithmic inefficiencies or optimization opportunities

## Code Quality
Style, readability, and maintainability suggestions

## Positive Aspects
What the code does well

## Recommendations
Specific actionable improvements

Be specific, cite line numbers or code snippets when possible, and explain WHY each issue matters.
"""

        if ctx:
            await ctx.report_progress(0, 1, "Performing detailed code review...")

        # Create progress callback
        async def progress_callback(message: str):
            if ctx:
                await ctx.report_progress(0, 1, message)

        # Use extended timeout for thorough reviews
        response = await client.query(
            prompt=review_prompt,
            model=model,
            timeout=settings.default_timeout * 2,
            progress_callback=progress_callback if ctx else None,
        )

        if ctx:
            await ctx.report_progress(1, 1, "Code review complete")
            await ctx.info("Code review completed successfully")

        return {
            "review": response.content,
            "model": response.model,
            "success": response.success,
        }

    except GeminiError as e:
        if ctx:
            await ctx.error(f"Code review failed: {e.message}")
        raise ToolError(f"Code review failed: {e.message}") from e
