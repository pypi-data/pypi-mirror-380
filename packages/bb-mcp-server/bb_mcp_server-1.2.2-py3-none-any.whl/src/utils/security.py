"""
Security configuration for Bitbucket MCP Server
HTTP-only transport helpers and logging guidance
"""

import os
from typing import Optional

from fastmcp.utilities.logging import get_logger

logger = get_logger(__name__)


# Simple bearer token authentication implementation
class SimpleBearerAuth:
    """Simple bearer token authentication for FastMCP servers."""

    def __init__(self, tokens: list[str]):
        """Initialize with a list of valid tokens."""
        self.valid_tokens = set(tokens)

    async def authenticate(self, headers: dict) -> bool:
        """Check if the request has a valid bearer token."""
        auth_header = headers.get("authorization", "")
        if auth_header.startswith("Bearer "):
            token = auth_header[7:]
            return token in self.valid_tokens
        return False


def get_server_auth(_: Optional[str] = None):
    """Return HTTP authentication configuration placeholder."""
    auth_token = os.getenv("MCP_AUTH_TOKEN")

    if auth_token:
        logger.info("HTTP transport detected - enabling Bearer token authentication")
    else:
        logger.warning(
            "HTTP server running without MCP_AUTH_TOKEN! "
            "Set MCP_AUTH_TOKEN to protect your server."
        )

    # Authentication is enforced by middleware; keep API for compatibility
    return None


def should_require_client_credentials(_: Optional[str] = None) -> bool:
    """Determine if clients must provide Bitbucket credentials via headers."""
    has_server_creds = bool(
        os.getenv("BITBUCKET_USERNAME") and
        os.getenv("BITBUCKET_APP_PASSWORD")
    )

    if not has_server_creds:
        return True

    return os.getenv("REQUIRE_CLIENT_CREDENTIALS", "false").lower() == "true"


def validate_credentials(config) -> bool:
    """
    Validate that necessary credentials are available

    Args:
        config: Config instance to validate

    Returns:
        True if valid credentials are available
    """
    # Check for auth token (Bearer) first
    if config.auth_token:
        return True

    # Check for username/password
    if config.username and config.app_password:
        return True

    return False


def get_security_warnings(_: Optional[str] = None) -> list[str]:
    """List HTTP security warnings for the current configuration."""
    warnings = []

    if not os.getenv("MCP_AUTH_TOKEN"):
        warnings.append(
            "⚠️  HTTP server running without authentication! "
            "Set MCP_AUTH_TOKEN to protect your server."
        )

    if os.getenv("BITBUCKET_USERNAME") and os.getenv("BITBUCKET_APP_PASSWORD"):
        if not os.getenv("REQUIRE_CLIENT_CREDENTIALS"):
            warnings.append(
                "⚠️  Server is using embedded Bitbucket credentials. "
                "Consider setting REQUIRE_CLIENT_CREDENTIALS=true for multi-tenant mode."
            )

    return warnings
