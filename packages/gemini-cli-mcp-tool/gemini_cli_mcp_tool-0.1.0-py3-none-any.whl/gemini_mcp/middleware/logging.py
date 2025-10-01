"""Structured logging middleware for FastMCP server."""

from collections.abc import Awaitable, Callable
from typing import Any

from fastmcp.server.middleware import Middleware, MiddlewareContext
import structlog

logger = structlog.get_logger(__name__)


class LoggingMiddleware(Middleware):
    """Middleware for structured request/response logging.

    Provides comprehensive logging of all MCP operations with structured
    metadata for observability and debugging.
    """

    async def on_message(
        self,
        context: MiddlewareContext,
        call_next: Callable[[MiddlewareContext], Awaitable[Any]],
    ) -> Any:
        """Log request and response information.

        Args:
            context: Middleware context containing request information
            call_next: Next middleware/handler in the chain

        Returns:
            Response from the handler
        """
        logger.info(
            "Received MCP request",
            method=context.method,
            message_id=getattr(context.message, "id", None),
        )

        try:
            response = await call_next(context)

            logger.info(
                "Request completed successfully",
                method=context.method,
                message_id=getattr(context.message, "id", None),
            )

            return response

        except Exception:
            logger.error(
                "Request failed",
                method=context.method,
                message_id=getattr(context.message, "id", None),
            )
            raise
