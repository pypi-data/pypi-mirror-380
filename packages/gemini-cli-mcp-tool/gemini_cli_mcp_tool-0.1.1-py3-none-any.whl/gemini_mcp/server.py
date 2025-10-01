"""Main FastMCP server entry point.

This module sets up and runs the Gemini CLI MCP server with all tools,
middleware, and configuration.
"""

from fastmcp import FastMCP
import structlog

from gemini_mcp.config import get_settings
from gemini_mcp.middleware import GeminiErrorMiddleware, LoggingMiddleware
from gemini_mcp.tools import (
    gemini_analyze_codebase,
    gemini_code_review,
    gemini_context_query,
    gemini_query,
)

# Configure structured logging
structlog.configure(
    processors=[
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.dev.ConsoleRenderer(),
    ],
    wrapper_class=structlog.stdlib.BoundLogger,
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger(__name__)


def create_server() -> FastMCP:
    """Create and configure the FastMCP server instance.

    Returns:
        Configured FastMCP server
    """
    settings = get_settings()

    # Create server with production settings
    mcp = FastMCP(
        name=settings.server_name,
        mask_error_details=settings.mask_error_details,
    )

    # Add middleware (order matters: logging first, then error handling)
    mcp.add_middleware(LoggingMiddleware())
    mcp.add_middleware(GeminiErrorMiddleware(mask_details=settings.mask_error_details))

    # Register tools
    mcp.tool(gemini_query)
    mcp.tool(gemini_context_query)
    mcp.tool(gemini_analyze_codebase)
    mcp.tool(gemini_code_review)

    logger.info(
        "Server initialized",
        server_name=settings.server_name,
        log_level=settings.log_level,
    )

    return mcp


# Create server instance
server = create_server()


def main() -> None:
    """Run the MCP server.

    This is the entry point for the gemini-mcp CLI command.
    """
    settings = get_settings()

    logger.info(
        "Starting Gemini MCP Server",
        server_name=settings.server_name,
        model=settings.default_model,
    )

    # Run server with STDIO transport (default for MCP)
    server.run()


if __name__ == "__main__":
    main()
