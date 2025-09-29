"""
Authentication Middleware for Bitbucket MCP Server
Provides bearer token authentication for HTTP transport
"""

import os
from typing import Optional

from fastmcp.server.middleware import Middleware, MiddlewareContext
from fastmcp.utilities.logging import get_logger

logger = get_logger(__name__)


class BearerAuthMiddleware(Middleware):
    """
    Middleware that validates bearer tokens for HTTP requests.
    Only active when MCP_AUTH_TOKEN is set.
    """

    def __init__(self):
        """Initialize the auth middleware."""
        super().__init__()
        self.auth_token = os.getenv("MCP_AUTH_TOKEN")
        self.enabled = bool(self.auth_token)

        if self.enabled:
            logger.info("Bearer token authentication enabled")
        else:
            logger.warning("Bearer token authentication disabled - no MCP_AUTH_TOKEN set")

    async def on_request(self, context: MiddlewareContext, call_next):
        """
        Check bearer token on all requests if authentication is enabled.
        """
        # Try to get headers
        headers = self._get_headers(context)

        self._store_request_config(context, headers)

        # Skip auth if not enabled
        if not self.enabled:
            return await call_next(context)

        # Check authorization header
        auth_header = headers.get("authorization", "")

        if not auth_header.startswith("Bearer "):
            # No bearer token provided
            raise ValueError("Authentication required: Missing Bearer token")

        token = auth_header[7:]  # Remove "Bearer " prefix

        if token != self.auth_token:
            # Invalid token
            raise ValueError("Authentication failed: Invalid token")

        # Token is valid, continue
        return await call_next(context)

    def _store_request_config(self, context: MiddlewareContext, headers: dict[str, str]) -> None:
        """Persist per-request configuration in the FastMCP context state."""
        fastmcp_ctx = context.fastmcp_context
        if fastmcp_ctx is None:
            return

        from src.utils.config import Config, CONTEXT_CONFIG_KEY

        existing = fastmcp_ctx.get_state(CONTEXT_CONFIG_KEY)
        if existing is not None and not headers:
            # Keep the previous config when no new headers were provided
            return

        config = Config(headers or None)
        fastmcp_ctx.set_state(CONTEXT_CONFIG_KEY, config)

    def _get_headers(self, context: MiddlewareContext) -> dict:
        """Extract headers from the context."""
        try:
            # Try FastMCP's get_http_headers if available
            from fastmcp.server.dependencies import get_http_headers
            headers = get_http_headers()
            logger.info("🚀 ~ headers:", headers)
            if headers:
                return {k.lower(): v for k, v in headers.items()}
        except:
            pass

        # Fallback to empty dict when headers are unavailable
        return {}
