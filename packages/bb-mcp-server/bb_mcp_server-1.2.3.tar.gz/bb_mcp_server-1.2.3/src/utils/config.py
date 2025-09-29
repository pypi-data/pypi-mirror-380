"""
Configuration module for Bitbucket MCP Server
Handles environment variables and HTTP header-based configuration
"""

import os
from typing import Any, Dict, Optional

from dotenv import load_dotenv
from urllib.parse import parse_qs
from fastmcp import Context
from fastmcp.server.dependencies import get_context, get_http_headers, get_http_request
from fastmcp.utilities.logging import get_logger

logger = get_logger(__name__)

# Load environment variables from .env file
load_dotenv()


class Config:
    """
    Configuration class that can retrieve settings from multiple sources:
    1. HTTP headers supplied with each request
    2. Environment variables provided as server defaults
    3. Fallback default values
    """

    def __init__(self, headers: Optional[Dict[str, str]] = None):
        """
        Initialize configuration with optional HTTP headers

        Args:
            headers: Optional HTTP headers dict for HTTP/SSE connections
        """
        self.headers = headers or get_http_headers()
        self._cached_values: Dict[str, Any] = {}

    def get(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value from headers (with X- prefix) or environment

        Priority order:
        1. HTTP header (X-BITBUCKET-{KEY} or X-{KEY})
        2. Environment variable (BITBUCKET_{KEY} or {KEY}) - only if allowed
        3. Default value
        """
        # Check cache first
        if key in self._cached_values:
            return self._cached_values[key]

        # Try HTTP headers first (case-insensitive)
        if self.headers:
            # Try with X-BITBUCKET- prefix
            header_key = f"X-BITBUCKET-{key}".replace('_', '-')
            
            for h_key, h_val in self.headers.items():
                if h_key.upper() == header_key.upper():
                    self._cached_values[key] = h_val
                    
                    return h_val

            # Try with just X- prefix
            header_key = f"X-{key}".replace('_', '-')
            for h_key, h_val in self.headers.items():
                if h_key.upper() == header_key.upper():
                    self._cached_values[key] = h_val
                    
                    return h_val

        # Try environment variables (with security check for HTTP mode)
        # Skip env vars for sensitive data if client should provide credentials
        sensitive_keys = ["USERNAME", "APP_PASSWORD", "WORKSPACE", "REPO"]
        is_sensitive = key.upper() in sensitive_keys

        # In HTTP mode with REQUIRE_CLIENT_CREDENTIALS, don't use server env for sensitive data
        if is_sensitive and self.headers and os.getenv("REQUIRE_CLIENT_CREDENTIALS", "false").lower() == "true":
            # Don't use server's credentials, require client to provide them
            self._cached_values[key] = default
            
            
            return default

        # First try with BITBUCKET_ prefix
        env_key = f"BITBUCKET_{key}"
        value = os.getenv(env_key)
        if value is not None:
            self._cached_values[key] = value
            return value

        # Then try without prefix
        value = os.getenv(key)
        if value is not None:
            self._cached_values[key] = value
            return value

        # Return default
        self._cached_values[key] = default
        
        return default

    def get_bool(self, key: str, default: bool = False) -> bool:
        """Get configuration value as boolean"""
        value = self.get(key)
        if value is None:
            return default
        if isinstance(value, bool):
            return value
        # Convert string to bool
        return str(value).lower() in ('true', '1', 'yes', 'on')

    @property
    def workspace(self) -> str:
        """Get workspace configuration"""
        return self.get("WORKSPACE", "")

    @property
    def repo_slug(self) -> str:
        """Get repository slug configuration"""
        return self.get("REPO", "")

    @property
    def username(self) -> Optional[str]:
        """Get Bitbucket username"""
        return self.get("USERNAME")

    @property
    def app_password(self) -> Optional[str]:
        """Get Bitbucket app password"""
        return self.get("APP_PASSWORD")

    @property
    def no_tools(self) -> bool:
        """Check if tools should be disabled"""
        return self.get_bool("NO_TOOLS", False)

    @property
    def auth_token(self) -> Optional[str]:
        """Get Bearer auth token from Authorization header"""
        if self.headers:
            auth_header = self.headers.get("Authorization") or self.headers.get("authorization")
            if auth_header and auth_header.startswith("Bearer "):
                return auth_header[7:]  # Remove "Bearer " prefix
        return None


# Context state key for per-request configuration
CONTEXT_CONFIG_KEY = "bitbucket_config"

# Global configuration instance (process-level fallback for startup tasks)
_global_config = Config()

# Legacy exports for backward compatibility
WORKSPACE = _global_config.workspace
REPO_SLUG = _global_config.repo_slug
BITBUCKET_USERNAME = _global_config.username
BITBUCKET_APP_PASSWORD = _global_config.app_password
NO_TOOLS = _global_config.no_tools

# API Configuration
BASE_URL = "https://api.bitbucket.org/2.0"
DEFAULT_TIMEOUT = 30.0

# Server Configuration
SERVER_NAME = "bitbucket_mcp"
SERVER_INSTRUCTIONS = """An essential toolset for common Bitbucket workflows including pipelines, pull requests, and repository management"""

def _get_context_config() -> Optional[Config]:
    """Retrieve configuration stored in the active FastMCP context."""
    try:
        ctx = get_context()
    except RuntimeError:
        return None

    if ctx is None:
        return None

    config = ctx.get_state(CONTEXT_CONFIG_KEY)
    if config is None:
        headers = get_http_headers()
        if headers:
            config = Config(headers)
            ctx.set_state(CONTEXT_CONFIG_KEY, config)
    return config


def _apply_request_overrides(config: Config) -> Config:
    """Apply repo/workspace overrides from the active HTTP request if present."""
    try:
        request = get_http_request()
    except RuntimeError:
        return config

    global _global_config
    if config is _global_config:
        base_headers = dict(getattr(config, "headers", {}) or {})
        config = Config(base_headers)

    query_repo = (request.query_params.get("repo") or "").strip()
    if query_repo:
        extra_workspace = None
        if "?" in query_repo:
            repo_slug, extra = query_repo.split("?", 1)
            repo_slug = repo_slug.strip()
            extra_params = parse_qs(extra, keep_blank_values=False)
            workspace_candidates = extra_params.get("workspace") or extra_params.get("workspaces")
            if workspace_candidates:
                extra_workspace = (workspace_candidates[0] or "").strip()
        else:
            repo_slug = query_repo

        workspace = None
        if "/" in repo_slug:
            workspace, repo_slug = repo_slug.split("/", 1)
            workspace = workspace.strip()
            repo_slug = repo_slug.strip()
        repo_slug = repo_slug.strip()

        if workspace:
            _cache_config_value(config, "WORKSPACE", workspace, override=True)
        if extra_workspace:
            _cache_config_value(config, "WORKSPACE", extra_workspace, override=True)
        if repo_slug:
            _cache_config_value(config, "REPO", repo_slug, override=True)

    query_workspace = (request.query_params.get("workspace") or "").strip()
    if query_workspace:
        _cache_config_value(config, "WORKSPACE", query_workspace, override=True)

    return config


def _cache_config_value(config: Config, key: str, value: str, *, override: bool = False) -> None:
    if not value:
        return
    headers = dict(getattr(config, "headers", {}) or {})
    header_key = None
    if key == "WORKSPACE":
        header_key = "X-BITBUCKET-WORKSPACE"
    elif key == "REPO":
        header_key = "X-BITBUCKET-REPO"

    if header_key:
        if override or header_key not in headers:
            headers[header_key] = value
    config.headers = headers
    cache = getattr(config, "_cached_values", None)
    if isinstance(cache, dict):
        cache[key] = value


def get_config(headers: Optional[Dict[str, str]] = None) -> Config:
    logger.debug(f"get_config: {headers}")
    """Get a configuration instance, optionally with HTTP headers."""

    if headers:
        config_headers = Config(headers)
        logger.debug(f"🥸 config_headers: {config_headers}")
        return config_headers

    context_config = _get_context_config()
    if context_config:
        context_config = _apply_request_overrides(context_config)
        logger.debug(f"🥸 context_config: {context_config}")
        return context_config

    global_config = _apply_request_overrides(_global_config)
    logger.debug(f"🥸 _global_config: {global_config}")
    return global_config

    logger.debug(f"🥸 _global_config: {_global_config}")
    return _global_config


def update_global_config(headers: Optional[Dict[str, str]] = None):
    """
    Update the global configuration with HTTP headers
    This should be called early in the request lifecycle for HTTP/SSE connections
    """
    global _global_config
    _global_config = Config(headers)


def get_config_for_context(ctx: Context | None) -> Config:
    """Return configuration bound to the provided FastMCP context."""
    if ctx is None:
        return get_config()

    config = ctx.get_state(CONTEXT_CONFIG_KEY)
    if isinstance(config, Config):
        return config

    headers = get_http_headers()
    if headers:
        config = Config(headers)
    else:
        config = Config()

    ctx.set_state(CONTEXT_CONFIG_KEY, config)
    return config
