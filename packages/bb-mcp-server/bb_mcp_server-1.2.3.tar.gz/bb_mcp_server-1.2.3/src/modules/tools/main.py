"""Tool registration for the lean Bitbucket toolset."""

from __future__ import annotations

from typing import Iterable

import inspect

from fastmcp.tools import Tool
from fastmcp.utilities.logging import get_logger

from .meta import pipe_fail_summary, pr_overview, pr_review
from .schemas import TOOL_SPECS
from .tools import (me_whoami, pipe_run, pr_comment_add, pr_list,
                    pr_tasks_sync, pr_upsert, repo_get, workspace_list)

logger = get_logger(__name__)


TOOL_REGISTRY = {
    "pr.list": pr_list,
    "pr.overview": pr_overview,
    "pr.review": pr_review,
    "pr.comment.add": pr_comment_add,
    "pr.upsert": pr_upsert,
    "pr.tasks.sync": pr_tasks_sync,
    "pipe.run": pipe_run,
    "pipe.fail.summary": pipe_fail_summary,
    "workspace.list": workspace_list,
    "repo.get": repo_get,
    "me.whoami": me_whoami,
}

def _is_enabled(name: str, func_name: str, allowed: Iterable[str]) -> bool:
    allowed = list(allowed or [])
    if not allowed:
        return True
    lowered = {item.lower() for item in allowed}
    if name.lower() in lowered or func_name.lower() in lowered:
        return True
    return False


async def init(mcp, allowed_tools: list[str]) -> None:
    """Register lean tools with compact schemas."""

    for name, func in TOOL_REGISTRY.items():
        spec = TOOL_SPECS.get(name, {})
        enabled = _is_enabled(name, func.__name__, allowed_tools)
        exclude_args = ["ctx"]
        params = inspect.signature(func).parameters
        if "repo" in params:
            exclude_args.append("repo")
        if "workspace" in params:
            exclude_args.append("workspace")

        # Deduplicate while preserving order
        seen: set[str] = set()
        exclude_args = [arg for arg in exclude_args if not (arg in seen or seen.add(arg))]

        tool = Tool.from_function(
            func,
            name=name,
            description=spec.get("description"),
            output_schema=spec.get("output_schema"),
            exclude_args=exclude_args or None,
            enabled=enabled,
        )
        mcp.add_tool(tool)
        if enabled:
            logger.debug(f"Enabled tool: {name}")

    logger.info(f"Registered {len(TOOL_REGISTRY)} lean tools.")
