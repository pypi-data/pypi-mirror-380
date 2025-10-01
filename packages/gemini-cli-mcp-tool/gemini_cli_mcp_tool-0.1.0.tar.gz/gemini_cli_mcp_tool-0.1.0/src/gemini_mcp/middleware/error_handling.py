"""Error handling middleware for FastMCP server.

Provides comprehensive error handling and transformation following best practices.
"""

from collections.abc import Awaitable, Callable
from typing import Any

from fastmcp.server.middleware import Middleware, MiddlewareContext
import structlog

logger = structlog.get_logger(__name__)


class GeminiErrorMiddleware(Middleware):
    """Middleware for comprehensive error handling and transformation.

    This middleware catches exceptions during tool execution, logs them
    with structured logging, and ensures consistent error responses
    following FastMCP best practices.
    """

    def __init__(self, mask_details: bool = True) -> None:
        """Initialize error handling middleware.

        Args:
            mask_details: Whether to mask internal error details
                (recommended for production)
        """
        self.mask_details = mask_details
        self.error_counts: dict[str, int] = {}

    async def on_message(
        self,
        context: MiddlewareContext,
        call_next: Callable[[MiddlewareContext], Awaitable[Any]],
    ) -> Any:
        """Handle message with comprehensive error handling.

        Args:
            context: Middleware context containing request information
            call_next: Next middleware/handler in the chain

        Returns:
            Response from the handler or error response

        Raises:
            Exception: Re-raises after logging for proper MCP error handling
        """
        try:
            return await call_next(context)

        except Exception as error:
            # Track error statistics
            error_key = f"{type(error).__name__}:{context.method}"
            self.error_counts[error_key] = self.error_counts.get(error_key, 0) + 1

            # Log with structured logging
            logger.error(
                "Error processing message",
                error_type=type(error).__name__,
                error_message=str(error),
                method=context.method,
                error_count=self.error_counts[error_key],
                exc_info=not self.mask_details,
            )

            # Re-raise to let FastMCP handle the error response
            raise

    def get_error_stats(self) -> dict[str, int]:
        """Get error statistics.

        Returns:
            Dictionary mapping error patterns to counts
        """
        return self.error_counts.copy()
