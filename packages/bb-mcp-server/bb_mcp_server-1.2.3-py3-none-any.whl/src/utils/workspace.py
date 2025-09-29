"""Workspace resolution helpers for Bitbucket MCP server."""

from __future__ import annotations

import os
from typing import Any

from fastmcp.utilities.logging import get_logger

from src.utils.api_client import make_request
from src.utils.config import Config, update_global_config

logger = get_logger(__name__)


async def ensure_workspace(config: Config) -> str:
    """Ensure the Bitbucket workspace is known, attempting auto-discovery if absent.

    Args:
        config: Active configuration instance containing credentials.

    Returns:
        The resolved workspace slug.

    Raises:
        ValueError: If no workspace can be determined automatically or multiple
            workspaces are available.
    """

    workspace = (config.workspace or "").strip()
    if workspace:
        return workspace

    logger.info("Workspace not provided; attempting auto-discovery via Bitbucket API")

    response = await make_request(
        "GET",
        "workspaces",
        params={"role": "member"},
        config=config,
    )

    values: list[dict[str, Any]] = response.get("values") or []
    if not values:
        raise ValueError(
            "Unable to determine Bitbucket workspace automatically. Provide the "
            "X-Bitbucket-Workspace header or BITBUCKET_WORKSPACE environment variable."
        )

    slugs = [
        (item or {}).get("slug")
        or ((item or {}).get("workspace") or {}).get("slug")
        for item in values
    ]
    slugs = [slug for slug in slugs if slug]

    if not slugs:
        raise ValueError(
            "Bitbucket workspace discovery returned results without slugs. "
            "Provide the workspace explicitly."
        )

    unique_slugs = sorted(set(slugs))
    if len(unique_slugs) > 1:
        pretty = ", ".join(unique_slugs)
        raise ValueError(
            "Multiple Bitbucket workspaces detected (" + pretty + "). "
            "Provide the desired workspace via header or environment."
        )

    resolved = unique_slugs[0]
    logger.info(f"Auto-discovered Bitbucket workspace '{resolved}'")

    os.environ.setdefault("BITBUCKET_WORKSPACE", resolved)

    # Update current config caches/headers so the workspace is visible immediately.
    try:
        config.headers = {**(config.headers or {}), "X-BITBUCKET-WORKSPACE": resolved}
    except Exception:
        pass
    try:
        config._cached_values["WORKSPACE"] = resolved
    except Exception:
        pass

    # Refresh the global configuration so future get_config() calls see the workspace.
    update_global_config()

    return resolved
