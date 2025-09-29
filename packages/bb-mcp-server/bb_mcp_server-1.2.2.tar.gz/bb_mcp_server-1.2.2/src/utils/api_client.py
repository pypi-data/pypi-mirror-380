"""
API Client module for Bitbucket MCP Server
Handles HTTP requests to Bitbucket API with authentication
"""

from typing import Any, Dict, Optional

import httpx
from fastmcp.utilities.logging import get_logger

from src.utils.auth import get_auth_headers
from src.utils.config import BASE_URL, DEFAULT_TIMEOUT, Config, get_config

try:
    from fastmcp.server.dependencies import get_http_headers
except ImportError:
    # Fallback if not available
    def get_http_headers():
        return {}

logger = get_logger(__name__)


async def make_request(method: str,
                       endpoint: str,
                       params: Optional[Dict] = None,
                       json_data: Optional[Dict] = None,
                       headers: Optional[Dict] = None,
                       accept_type: Optional[str] = None,
                       config: Optional[Config] = None) -> Dict[str, Any]:
    """
    Make authenticated request to Bitbucket API

    Args:
        method: HTTP method (GET, POST, PUT, DELETE)
        endpoint: API endpoint path
        params: Query parameters
        json_data: JSON body data
        headers: Additional headers
        accept_type: Override Accept header for specific content types
        config: Optional Config instance for request-specific configuration

    Returns:
        Dict containing response data

    Raises:
        httpx.HTTPStatusError: If request fails
    """
    # Use provided config or create one with current HTTP headers
    if config is None:
        # Try to get HTTP headers if we're in HTTP mode
        headers_dict = get_http_headers()
        if headers_dict:
            logger.error(f"DEBUG: header keys: {list(headers_dict.keys())}")
        config = get_config()

    # Build URL with dynamic workspace and repo from config
    url = f"{BASE_URL}/{endpoint}"
    # Replace placeholders in endpoint with actual values from config
    url = url.replace("{workspace}", config.workspace)
    url = url.replace("{repo_slug}", config.repo_slug)

    auth_headers = get_auth_headers(config)

    # Override Accept header if specified (needed for pipeline logs)
    if accept_type:
        auth_headers["Accept"] = accept_type

    # Merge additional headers
    if headers:
        auth_headers.update(headers)

    # Create client with redirect following enabled (needed for diffstat)
    async with httpx.AsyncClient(follow_redirects=True) as client:
        try:
            response = await client.request(method=method,
                                            url=url,
                                            params=params,
                                            json=json_data,
                                            headers=auth_headers,
                                            timeout=DEFAULT_TIMEOUT)
            response.raise_for_status()

            content_type = response.headers.get("content-type", "")
            if content_type.startswith(("text/", "application/octet-stream")):
                return {"content": response.text}

            return response.json()

        except httpx.HTTPStatusError as e:
            # Try to extract detailed error message from Bitbucket API response
            error_detail = ""
            try:
                error_body = e.response.json()
                if "error" in error_body:
                    error_info = error_body["error"]
                    if isinstance(error_info, dict):
                        error_detail = error_info.get("message", "")
                        if "detail" in error_info:
                            error_detail += f" - {error_info['detail']}"
                        if "fields" in error_info:
                            # Include field-specific errors
                            field_errors = []
                            for field, messages in error_info["fields"].items():
                                field_errors.append(f"{field}: {', '.join(messages)}")
                            if field_errors:
                                error_detail += f" - Fields: {'; '.join(field_errors)}"
                    else:
                        error_detail = str(error_info)
                elif "message" in error_body:
                    error_detail = error_body["message"]
                elif "detail" in error_body:
                    error_detail = error_body["detail"]
                else:
                    error_detail = str(error_body)
            except (ValueError, KeyError):
                # If we can't parse the error response, use the raw text
                error_detail = e.response.text[:500] if e.response.text else ""

            # Log the detailed error
            logger.error(f"Bitbucket API error: {e.response.status_code} - {error_detail}")

            # Raise a more informative error
            if error_detail:
                raise httpx.HTTPStatusError(
                    f"{e.response.status_code} {e.response.reason_phrase}: {error_detail}",
                    request=e.request,
                    response=e.response
                )
            else:
                raise
