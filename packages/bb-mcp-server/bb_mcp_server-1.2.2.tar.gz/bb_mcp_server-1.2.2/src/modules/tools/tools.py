"""Lean Bitbucket tool implementations.

This module contains the compact tool surface described in
`lean-migration-strategy.md`. Responsibilities:

* Provide lightweight, summary-first responses.
* Offer short parameter names with sensible defaults.
* Keep helper utilities private to avoid polluting the tool list.
"""

from __future__ import annotations

from enum import Enum
from typing import Annotated, Any, Iterable, Literal, Optional, Sequence

from fastmcp import Context
from fastmcp.server.dependencies import get_context
from fastmcp.utilities.logging import get_logger
from pydantic import Field

from src.utils.api_client import make_request
from src.utils.config import BASE_URL, Config, get_config_for_context

logger = get_logger(__name__)

class Verbosity(Enum):
    """Verbosity levels for tool responses."""

    ids = "ids"
    summary = "summary"
    full = "full"


def _resolve_repo(repo: Optional[str], ctx: Context | None = None) -> tuple[str, str]:
    """Resolve workspace/repo slug using config defaults."""
    config = get_config_for_context(ctx)
    workspace = config.workspace
    repo_slug = config.repo_slug
    if repo:
        repo = repo.strip()
        if "/" in repo:
            workspace, repo_slug = repo.split("/", 1)
        else:
            repo_slug = repo

    if not workspace or not repo_slug:
        raise ValueError(
            "Missing Bitbucket workspace/repo. Configure BITBUCKET_WORKSPACE and BITBUCKET_REPO."
        )

    return workspace, repo_slug


def _normalize_cursor(cursor: str) -> str:
    """Convert an absolute Bitbucket URL into the relative endpoint path."""
    cursor = cursor.strip()
    if cursor.startswith(BASE_URL):
        cursor = cursor[len(BASE_URL) :]
    return cursor.lstrip("/")


def _bounded_pagelen(limit: int, default: int, maximum: int = 50) -> int:
    """Clamp limit into Bitbucket's pagelen bounds."""
    if limit is None:
        return default
    return max(1, min(limit, maximum))


def _escape_query_value(value: str) -> str:
    """Escape double quotes in Bitbucket query values."""

    return value.replace("\"", "\\\"")


async def _find_open_pr_by_branch(
    workspace: str,
    repo_slug: str,
    source_branch: Optional[str],
    destination_branch: Optional[str],
    config: Config | None = None,
) -> Optional[dict[str, Any]]:
    """Return the most recent open PR matching the branch criteria."""

    if not source_branch:
        return None

    query_parts = [f'source.branch.name="{_escape_query_value(source_branch)}"', 'state="OPEN"']
    if destination_branch:
        query_parts.append(
            f'destination.branch.name="{_escape_query_value(destination_branch)}"'
        )

    response = await make_request(
        "GET",
        f"repositories/{workspace}/{repo_slug}/pullrequests",
        params={
            "q": " AND ".join(query_parts),
            "pagelen": 1,
            "sort": "-updated_on",
            "fields": (
                "values.id,values.title,values.state,"
                "values.source.branch.name,values.destination.branch.name,"
                "values.links.html.href"
            ),
        },
        config=config,
    )

    values: list[dict[str, Any]] = response.get("values", []) or []
    if not values:
        return None
    return values[0]


def _build_reviewer_payload(reviewers: Sequence[str]) -> list[dict[str, str]]:
    """Translate reviewer identifiers into Bitbucket payload objects."""

    payload: list[dict[str, str]] = []
    for reviewer in reviewers:
        if not reviewer:
            continue
        value = reviewer.strip()
        if not value:
            continue
        if value.startswith("{") and value.endswith("}"):
            payload.append({"uuid": value})
            continue
        if value.startswith("uuid:"):
            payload.append({"uuid": value[5:].strip()})
            continue
        if value.startswith("account:"):
            payload.append({"account_id": value[8:].strip()})
            continue
        if value.startswith("account_id:"):
            payload.append({"account_id": value[11:].strip()})
            continue
        if value.startswith("nickname:"):
            payload.append({"nickname": value[9:].strip()})
            continue
        payload.append({"nickname": value})

    return payload


async def _current_user_uuid(
    config: Config | None = None,
    ctx: Context | None = None,
) -> Optional[str]:
    try:
        current_user = await make_request("GET", "user", config=config)
    except Exception as exc:  # pragma: no cover - network failure paths
        logger.warning(f"Failed to fetch current user: {exc}")
        if ctx:
            await ctx.warning(f"Failed to fetch current user: {exc}")
        return None
    return current_user.get("uuid")


def _summarize_pr_item(pr: dict[str, Any]) -> dict[str, Any]:
    participants = pr.get("participants", []) or []
    approvals = sum(1 for participant in participants if participant.get("approved"))

    task_count = pr.get("task_count") or {}
    tasks_open = (
        task_count.get("open")
        or task_count.get("pending")
        or task_count.get("total")
        or 0
    )

    return {
        "id": pr.get("id"),
        "title": pr.get("title", ""),
        "state": pr.get("state"),
        "approvals": approvals,
        "tasks_open": tasks_open,
        "updated": pr.get("updated_on") or pr.get("created_on"),
        "url": pr.get("links", {}).get("html", {}).get("href"),
    }


def _summarize_repo_item(repo: dict[str, Any]) -> dict[str, Any]:
    return {
        "slug": repo.get("slug"),
        "name": repo.get("name"),
        "is_private": repo.get("is_private", False),
        "url": repo.get("links", {}).get("html", {}).get("href"),
        "updated": repo.get("updated_on") or repo.get("created_on"),
    }

class PRState(Enum):
    OPEN = "OPEN"
    MERGED = "MERGED"
    DECLINED = "DECLINED"
    SUPERSEDED = "SUPERSEDED"
    ALL = "ALL"

async def pr_list(
    repo: Annotated[
        str | None,
        Field(
            description=(
                "Workspace/repository slug in 'workspace/repo' format. "
                "Falls back to configured defaults when omitted."
            )
        ),
    ] = None,
    author: Annotated[
        str,
        Field(description="Filter by author nickname; use 'me' for the current user."),
    ] = "me",
    state: Annotated[
        PRState,
        Field(description="Pull request state filter; pass null to include all states."),
    ] = PRState.OPEN,
    limit: Annotated[
        int,
        Field(description="Maximum pull requests to return.", ge=1, le=50),
    ] = 10,
    cursor: Annotated[
        str | None,
        Field(description="Pagination cursor from a previous response."),
    ] = None,
    verbosity: Annotated[
        Verbosity,
        Field(description="Response detail level: 'ids', 'summary', or 'full'."),
    ] = Verbosity.summary,
    ctx: Context | None = None,
) -> dict[str, Any]:
    """Summarize pull requests with compact metadata."""
    ctx = ctx or get_context()
    await ctx.debug("Listing pull requests")
    workspace, repo_slug = _resolve_repo(repo, ctx)
    config = get_config_for_context(ctx)

    endpoint: str
    params: Optional[dict[str, Any]]

    if cursor:
        endpoint = _normalize_cursor(cursor)
        params = None
    else:
        endpoint = f"repositories/{workspace}/{repo_slug}/pullrequests"
        params = {
            "pagelen": _bounded_pagelen(limit, default=10),
            "sort": "-updated_on",
            "fields": (
                "next,values.id,values.title,values.state,values.updated_on,"
                "values.created_on,values.links.html.href,values.task_count,"
                "values.participants.approved"
            ),
        }

        if state and state != PRState.ALL:
            params["state"] = state.value

        if author:
            author = author.strip()
            if author.lower() == "me":
                uuid = await _current_user_uuid(config, ctx)
                if uuid:
                    params["q"] = f'author.uuid="{uuid}"'
            else:
                params["q"] = f'author.nickname~"{author}"'

    response = await make_request("GET", endpoint, params=params, config=config)

    values: list[dict[str, Any]] = response.get("values", []) or []
    summaries = [_summarize_pr_item(pr) for pr in values]

    if verbosity == "ids":
        items: Iterable[Any] = [item["id"] for item in summaries]
    elif verbosity == "full":
        items = [dict(summary, raw=raw) for summary, raw in zip(summaries, values)]
    else:
        items = summaries

    next_cursor = response.get("next")
    if next_cursor:
        next_cursor = _normalize_cursor(next_cursor)

    return {
        "items": list(items),
        "next": next_cursor,
    }


async def pr_comment_add(
    pr: Annotated[str, Field(description="Pull request identifier (e.g. '123' or '#123').")],
    text: Annotated[str, Field(description="Markdown comment text to post.")],
    file: Annotated[
        str | None,
        Field(description="Optional file path for inline comment anchoring."),
    ] = None,
    line: Annotated[
        int | None,
        Field(description="Optional 1-based line number for inline comments.", ge=1),
    ] = None,
    repo: Annotated[
        str | None,
        Field(
            description=(
                "Workspace/repository slug in 'workspace/repo' format. "
                "Falls back to configured defaults when omitted."
            )
        ),
    ] = None,
    ctx: Context | None = None,
) -> dict[str, Any]:
    """Add a PR comment with an optional inline anchor."""

    if not text.strip():
        raise ValueError("Comment text cannot be empty.")

    ctx = ctx or get_context()
    workspace, repo_slug = _resolve_repo(repo, ctx)
    config = get_config_for_context(ctx)
    pr_id = str(pr).lstrip("#")

    payload: dict[str, Any] = {"content": {"raw": text}}

    if file or line:
        inline: dict[str, Any] = {}
        if file:
            inline["path"] = file
        if line is not None:
            inline["to"] = line
        if inline:
            payload["inline"] = inline

    result = await make_request(
        "POST",
        f"repositories/{workspace}/{repo_slug}/pullrequests/{pr_id}/comments",
        json_data=payload,
        config=config,
    )

    return {
        "id": result.get("id"),
        "url": result.get("links", {}).get("html", {}).get("href"),
    }


async def pr_tasks_sync(
    pr: Annotated[str, Field(description="Pull request identifier (e.g. '123' or '#123').")],
    create: Annotated[
        Sequence[dict[str, Any]] | None,
        Field(
            description=(
                "Tasks to create; each item may include 'text', 'file', and 'line'."
            )
        ),
    ] = None,
    resolve: Annotated[
        Sequence[str] | None,
        Field(description="Task identifiers to mark as resolved."),
    ] = None,
    repo: Annotated[
        str | None,
        Field(
            description=(
                "Workspace/repository slug in 'workspace/repo' format. "
                "Falls back to configured defaults when omitted."
            )
        ),
    ] = None,
    ctx: Context | None = None,
) -> dict[str, Any]:
    """Create and resolve pull request tasks in a single call."""

    ctx = ctx or get_context()
    workspace, repo_slug = _resolve_repo(repo, ctx)
    config = get_config_for_context(ctx)
    pr_id = str(pr).lstrip("#")

    base_endpoint = f"repositories/{workspace}/{repo_slug}/pullrequests/{pr_id}/tasks"

    created_ids: list[str] = []
    resolved_ids: list[str] = []

    for item in create or []:
        text = (item or {}).get("text", "").strip()
        if not text:
            continue

        payload: dict[str, Any] = {"content": {"raw": text}}
        if item.get("file") or item.get("line"):
            anchor: dict[str, Any] = {"type": "pullrequest"}
            if item.get("file"):
                anchor["path"] = item["file"]
            if item.get("line"):
                anchor["line"] = item["line"]
            payload["anchor"] = anchor

        task = await make_request("POST", base_endpoint, json_data=payload, config=config)
        task_id = str(task.get("id")) if task.get("id") is not None else None
        if task_id:
            created_ids.append(task_id)

    for task_id in resolve or []:
        task_id = str(task_id).strip()
        if not task_id:
            continue
        await make_request(
            "PUT",
            f"{base_endpoint}/{task_id}",
            json_data={"state": "RESOLVED"},
            config=config,
        )
        resolved_ids.append(task_id)

    tasks_response = await make_request(
        "GET",
        base_endpoint,
        params={
            "pagelen": 50,
            "fields": "values.id,values.state",
        },
        config=config,
    )

    remaining = sum(
        1
        for task in tasks_response.get("values", []) or []
        if task.get("state") != "RESOLVED"
    )

    return {
        "created": created_ids,
        "resolved": resolved_ids,
        "remaining": remaining,
    }


async def pr_upsert(
    title: Annotated[
        str | None,
        Field(description="Pull request title. Required when creating a PR."),
    ] = None,
    source: Annotated[
        str | None,
        Field(
            description="Source branch name. Used to detect or create the pull request.",
        ),
    ] = None,
    destination: Annotated[
        str | None,
        Field(
            description=(
                "Destination branch name. Required when creating unless the repo has a configured main branch."
            ),
        ),
    ] = None,
    summary: Annotated[
        str | None,
        Field(description="Optional Markdown summary/description for the PR."),
    ] = None,
    reviewers: Annotated[
        Sequence[str] | None,
        Field(
            description=(
                "Reviewer identifiers (uuid:{...}, account:{id}, nickname:{name}, or raw nickname). "
                "Find defaults via the workspace://{workspace}/default-reviewers resource or workspace.list tool."
            ),
        ),
    ] = None,
    close_source: Annotated[
        Literal[True, False],
        Field(description="Close the source branch on merge when True."),
    ] = False,
    draft: Annotated[
        Literal[True, False],
        Field(description="Create or update the PR as a draft."),
    ] = False,
    pr: Annotated[
        str | None,
        Field(
            description=(
                "Existing PR identifier to update. If omitted, the tool creates a new PR or updates the latest open PR for the source branch."
            ),
        ),
    ] = None,
    repo: Annotated[
        str | None,
        Field(
            description=(
                "Workspace/repository slug in 'workspace/repo' format. "
                "Falls back to configured defaults when omitted."
            )
        ),
    ] = None,
    ctx: Context | None = None,
) -> dict[str, Any]:
    """Create a new PR or update an existing one with concise metadata."""

    ctx = ctx or get_context()
    workspace, repo_slug = _resolve_repo(repo, ctx)
    config = get_config_for_context(ctx)

    pr_id: Optional[str] = str(pr).lstrip("#") if pr else None

    if not pr_id and source:
        existing = await _find_open_pr_by_branch(
            workspace,
            repo_slug,
            source,
            destination,
            config=config,
        )
        if existing:
            pr_id = str(existing.get("id")) if existing.get("id") is not None else None

    payload: dict[str, Any] = {}

    if title is not None:
        cleaned = title.strip()
        if not cleaned:
            raise ValueError("Title cannot be empty when provided.")
        payload["title"] = cleaned

    if summary is not None:
        payload["summary"] = {"raw": summary}

    if source is not None:
        if not source.strip():
            raise ValueError("Source branch name cannot be empty when provided.")
        payload["source"] = {"branch": {"name": source.strip()}}

    dest_branch = destination.strip() if destination else None

    if dest_branch is not None:
        if not dest_branch:
            raise ValueError("Destination branch name cannot be empty when provided.")
        payload["destination"] = {"branch": {"name": dest_branch}}

    reviewer_payload: Optional[list[dict[str, str]]] = None
    if reviewers is not None:
        reviewer_payload = _build_reviewer_payload(reviewers)
        payload["reviewers"] = reviewer_payload

    if close_source is not None:
        payload["close_source_branch"] = close_source

    if draft is not None:
        payload["draft"] = draft

    creating = pr_id is None

    if creating:
        if "title" not in payload:
            raise ValueError("Title is required when creating a pull request.")
        if "source" not in payload:
            if source is None:
                raise ValueError("Source branch is required when creating a pull request.")
        if "source" not in payload:
            # Guard if source was invalid/empty
            raise ValueError("Source branch name cannot be empty when creating a pull request.")

        if "destination" not in payload:
            if dest_branch is None:
                repo_details = await make_request(
                    "GET",
                    f"repositories/{workspace}/{repo_slug}",
                    params={"fields": "mainbranch.name"},
                    config=config,
                )
                dest_branch = repo_details.get("mainbranch", {}).get("name")
                if dest_branch:
                    payload["destination"] = {"branch": {"name": dest_branch}}
            if "destination" not in payload:
                raise ValueError(
                    "Destination branch is required when creating a pull request."
                )

        result = await make_request(
            "POST",
            f"repositories/{workspace}/{repo_slug}/pullrequests",
            json_data=payload,
            config=config,
        )
        action = "created"
    else:
        if not payload:
            raise ValueError("No updates provided; specify at least one field to modify.")

        result = await make_request(
            "PUT",
            f"repositories/{workspace}/{repo_slug}/pullrequests/{pr_id}",
            json_data=payload,
            config=config,
        )
        action = "updated"

    return {
        "action": action,
        "id": result.get("id"),
        "title": result.get("title"),
        "state": result.get("state"),
        "source": result.get("source", {}).get("branch", {}).get("name"),
        "destination": result.get("destination", {}).get("branch", {}).get("name"),
        "url": result.get("links", {}).get("html", {}).get("href"),
    }


async def pipe_run(
    ref: Annotated[
        str,
        Field(description="Branch name or commit hash to run the pipeline against."),
    ],
    spec: Annotated[
        str,
        Field(description="Pipeline selector: 'default' or a custom pattern."),
    ] = "default",
    repo: Annotated[
        str | None,
        Field(description="Workspace/repository slug in 'workspace/repo' format."),
    ] = None,
    ctx: Context | None = None,
) -> dict[str, Any]:
    """Start a Bitbucket pipeline for a branch or commit."""

    ctx = ctx or get_context()
    workspace, repo_slug = _resolve_repo(repo, ctx)
    config = get_config_for_context(ctx)

    target_payload: dict[str, Any] = {
        "type": "pipeline_ref_target",
        "ref_name": ref,
        "ref_type": "branch",
    }

    if len(ref) == 40:
        target_payload["ref_type"] = "commit"
        target_payload["commit"] = {"hash": ref}

    selector: dict[str, Any]
    if spec == "default":
        selector = {"type": "default"}
    else:
        selector = {"type": "custom", "pattern": spec}

    payload = {
        "target": target_payload,
        "selector": selector,
    }

    result = await make_request(
        "POST",
        f"repositories/{workspace}/{repo_slug}/pipelines/",
        json_data=payload,
        config=config,
    )

    return {
        "pipeline_id": result.get("uuid") or result.get("build_number"),
        "url": result.get("links", {}).get("html", {}).get("href"),
    }


async def workspace_list(
    kind: Annotated[
        Literal["repos", "members", "projects", "reviewers"],
        Field(description="Item type to list: repositories, members, reviewers, or projects."),
    ],
    workspace: Annotated[
        str | None,
        Field(description="Workspace slug to query; defaults to configured workspace."),
    ] = None,
    limit: Annotated[
        int,
        Field(description="Maximum results to return per page.", ge=1, le=50),
    ] = 20,
    cursor: Annotated[
        str | None,
        Field(description="Pagination cursor from a previous response."),
    ] = None,
    verbosity: Annotated[
        Verbosity,
        Field(description="Response detail level: 'ids', 'summary', or 'full'."),
    ] = Verbosity.summary,
    ctx: Context | None = None,
) -> dict[str, Any]:
    """List repositories, members, or projects for a workspace."""

    ctx = ctx or get_context()
    config = get_config_for_context(ctx)
    workspace = (workspace or config.workspace).strip()
    if not workspace:
        raise ValueError("Workspace is required for workspace.list")

    repo_slug = config.repo_slug.strip()

    if cursor:
        endpoint = _normalize_cursor(cursor)
        params = None
    else:
        match kind:
            case "repos":
                endpoint = f"repositories/{workspace}"
                params = {
                    "pagelen": _bounded_pagelen(limit, default=20),
                    "fields": (
                        "next,values.slug,values.name,values.updated_on,"
                        "values.links.html.href,values.is_private"
                    ),
                }
            case "members":
                endpoint = f"workspaces/{workspace}/members"
                params = {
                    "pagelen": _bounded_pagelen(limit, default=20),
                    "fields": (
                        "next,values.user.uuid,values.user.display_name,"
                        "values.user.account_id,values.user.links.html.href"
                    ),
                }
            case "projects":
                endpoint = f"workspaces/{workspace}/projects"
                params = {
                    "pagelen": _bounded_pagelen(limit, default=20),
                    "fields": "next,values.key,values.name,values.updated_on,values.links.html.href",
                }
            case "reviewers":
                if not repo_slug:
                    raise ValueError(
                        "Repository slug is required to list default reviewers. Configure BITBUCKET_REPO or provide headers."
                    )
                endpoint = f"repositories/{workspace}/{repo_slug}/default-reviewers"
                params = {
                    "pagelen": _bounded_pagelen(limit, default=20),
                    "fields": (
                        "next,values.uuid,values.nickname,values.display_name,"
                        "values.account_id,values.links.html.href"
                    ),
                }
            case _:
                raise ValueError(f"Unsupported kind '{kind}'")

    response = await make_request("GET", endpoint, params=params, config=config)
    values: list[dict[str, Any]] = response.get("values", []) or []

    if kind == "repos":
        items = [_summarize_repo_item(repo) for repo in values]
    elif kind == "members":
        items = []
        for member in values:
            user = member.get("user") or {}
            links = user.get("links") or {}
            html_link = links.get("html") or {}

            uuid = user.get("uuid")
            if not uuid:
                continue

            items.append(
                {
                    "uuid": uuid,
                    "display_name": user.get("display_name", ""),
                    "account_id": user.get("account_id", ""),
                    "url": html_link.get("href"),
                }
            )
    elif kind == "reviewers":
        items = []
        for reviewer in values:
            account_id = reviewer.get("account_id", "")
            uuid = reviewer.get("uuid", "")
            if not uuid:
                continue
            if uuid:
                uuid = uuid.strip()
                me = await _current_user_uuid()
                if me and uuid == me:       
                 continue
            items.append(
                {
                    "uuid": uuid,
                    "username": reviewer.get("nickname", ""),
                    "display_name": reviewer.get("display_name", ""),
                    "account_id": account_id,
                    "url": reviewer.get("links", {}).get("html", {}).get("href"),
                }
            )
    else:  # projects
        items = [
            {
                "key": project.get("key"),
                "name": project.get("name"),
                "updated": project.get("updated_on") or project.get("created_on"),
                "url": project.get("links", {}).get("html", {}).get("href"),
            }
            for project in values
        ]

    if verbosity == "ids":
        if kind == "repos":
            items = [item["slug"] for item in items]
        elif kind == "members":
            items = [item["uuid"] for item in items]
        elif kind == "reviewers":
            items = [item["uuid"] for item in items]
        else:
            items = [item["key"] for item in items]
    elif verbosity == "full":
        items = [dict(item, raw=raw) for item, raw in zip(items, values)]

    next_cursor = response.get("next")
    if next_cursor:
        next_cursor = _normalize_cursor(next_cursor)

    return {
        "items": list(items),
        "next": next_cursor,
    }


async def repo_get(
    slug: Annotated[
        str,
        Field(description="Repository slug or 'workspace/repo'; workspace inferred if omitted."),
    ],
    verbosity: Annotated[
        Verbosity,
        Field(description="Response detail level: 'ids', 'summary', or 'full'."),
    ] = Verbosity.summary,
    ctx: Context | None = None,
) -> dict[str, Any]:
    """Return repo basics plus a tiny PR sample."""

    if "/" in slug:
        workspace, repo_slug = slug.split("/", 1)
    else:
        config = get_config_for_context(ctx)
        workspace = config.workspace
        repo_slug = slug
        if not workspace:
            raise ValueError("Workspace is required when slug is not workspace/repo")

    config = get_config_for_context(ctx)

    repo = await make_request(
        "GET",
        f"repositories/{workspace}/{repo_slug}",
        params={
            "fields": (
                "slug,name,mainbranch.name,links.html.href,updated_on,"
                "is_private,has_issues,has_wiki,workspace.slug"
            ),
        },
        config=config,
    )

    pr_sample = await pr_list(
        repo=f"{workspace}/{repo_slug}",
        limit=5,
        verbosity=Verbosity.summary,
        ctx=ctx,
    )

    result = {
        "slug": repo.get("slug"),
        "default_branch": repo.get("mainbranch", {}).get("name"),
        "perms": [
            key
            for key, value in repo.items()
            if key.startswith("has_") and isinstance(value, bool) and value
        ],
        "recent_prs": pr_sample.get("items", [])[:5],
        "url": repo.get("links", {}).get("html", {}).get("href"),
    }

    if verbosity == "full":
        result["raw"] = repo

    return result


async def me_whoami(ctx: Context | None = None) -> dict[str, Any]:
    """Return minimal identity information for the authenticated user."""

    ctx = ctx or get_context()
    config = get_config_for_context(ctx)

    user = await make_request(
        "GET",
        "user",
        params={"fields": "uuid,display_name,nickname,account_id"},
        config=config,
    )

    workspaces = await make_request(
        "GET",
        "workspaces",
        params={"pagelen": 20, "fields": "values.slug"},
        config=config,
    )

    return {
        "user": {
            "uuid": user.get("uuid"),
            "display_name": user.get("display_name"),
            "nickname": user.get("nickname"),
            "account_id": user.get("account_id"),
        },
        "workspaces": [ws.get("slug") for ws in workspaces.get("values", []) if ws.get("slug")],
    }
