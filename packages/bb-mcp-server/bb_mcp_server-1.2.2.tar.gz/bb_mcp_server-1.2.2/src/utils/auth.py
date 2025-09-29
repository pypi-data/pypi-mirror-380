"""Authentication helpers for Bitbucket MCP Server."""

from base64 import b64encode
from typing import Dict, Optional

from fastmcp.utilities.logging import get_logger

from src.utils.config import Config, get_config

logger = get_logger(__name__)
console = logger


def get_auth_headers(config: Optional[Config] = None) -> Dict[str, str]:
    """Generate Bitbucket auth headers from available credentials."""

    console.info(f"🚀 ~ get_auth_headers - config: {config}")

    if config is None:
        config = get_config()
        console.info(f"🚀 ~ config: {config}")

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    incoming_auth = None
    source_headers = getattr(config, "headers", None) or {}
    for key, value in source_headers.items():
        if key.lower() == "authorization":
            incoming_auth = str(value)
            break

    if incoming_auth:
        scheme = incoming_auth.split(" ", 1)[0].lower()
        if scheme in {"bearer", "basic"}:
            headers["Authorization"] = incoming_auth
            return headers

    auth_token = config.auth_token
    if auth_token:
        headers["Authorization"] = f"Bearer {auth_token}"
        return headers

    username = config.username
    password = config.app_password

    if not username or not password:
        raise ValueError(
            "Authentication required. Provide either:\n"
            "1. Authorization header (Bearer or Basic), or\n"
            "2. X-BITBUCKET-USERNAME and X-BITBUCKET-APP-PASSWORD headers, or\n"
            "3. BITBUCKET_USERNAME and BITBUCKET_APP_PASSWORD environment variables"
        )

    credentials = f"{username}:{password}"
    encoded = b64encode(credentials.encode()).decode("ascii")
    headers["Authorization"] = f"Basic {encoded}"

    return headers
