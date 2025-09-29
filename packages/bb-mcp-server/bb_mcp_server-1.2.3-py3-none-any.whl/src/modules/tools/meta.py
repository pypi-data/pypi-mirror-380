"""Composed Bitbucket tools built on top of the lean cores."""

from __future__ import annotations

from typing import Any, Literal, Optional

from fastmcp import Context
from fastmcp.server.dependencies import get_context
from fastmcp.utilities.logging import get_logger

from src.utils.api_client import make_request
from src.utils.config import Config, get_config_for_context
from .tools import Verbosity, _normalize_cursor, _resolve_repo

logger = get_logger(__name__)


async def _fetch_pr(
    workspace: str,
    repo_slug: str,
    pr_id: str,
    config: Config | None = None,
) -> dict[str, Any]:
    fields = (
        "id,title,state,author.display_name,author.nickname,updated_on,"
        "created_on,links.html.href,participants.role,participants.approved,"
        "task_count,merge_status,source.branch.name,destination.branch.name,summary.raw"
    )
    return await make_request(
        "GET",
        f"repositories/{workspace}/{repo_slug}/pullrequests/{pr_id}",
        params={"fields": fields},
        config=config,
    )


async def _fetch_pr_statuses(
    workspace: str,
    repo_slug: str,
    pr_id: str,
    config: Config | None = None,
) -> list[dict[str, Any]]:
    response = await make_request(
        "GET",
        f"repositories/{workspace}/{repo_slug}/pullrequests/{pr_id}/statuses",
        params={"pagelen": 25, "fields": "values.state,values.name"},
        config=config,
    )
    return response.get("values", []) or []


async def _fetch_pr_diffstat(
    workspace: str,
    repo_slug: str,
    pr_id: str,
    config: Config | None = None,
) -> tuple[list[dict[str, Any]], Optional[str]]:
    response = await make_request(
        "GET",
        f"repositories/{workspace}/{repo_slug}/pullrequests/{pr_id}/diffstat",
        params={"pagelen": 20},
        config=config,
    )
    values: list[dict[str, Any]] = response.get("values", []) or []
    diff_items: list[dict[str, Any]] = []
    for item in values[:20]:
        new_path = item.get("new", {}).get("path")
        old_path = item.get("old", {}).get("path")
        path = new_path or old_path
        diff_items.append(
            {
                "path": path,
                "add": item.get("lines_added", 0),
                "del": item.get("lines_removed", 0),
            }
        )

    next_cursor = response.get("next")
    if next_cursor:
        next_cursor = _normalize_cursor(next_cursor)

    return diff_items, next_cursor


async def _fetch_recent_comments(
    workspace: str,
    repo_slug: str,
    pr_id: str,
    config: Config | None = None,
) -> tuple[list[dict[str, Any]], Optional[str]]:
    response = await make_request(
        "GET",
        f"repositories/{workspace}/{repo_slug}/pullrequests/{pr_id}/comments",
        params={"pagelen": 5, "sort": "-created_on"},
        config=config,
    )
    comments: list[dict[str, Any]] = []
    for comment in response.get("values", []) or []:
        raw_text = comment.get("content", {}).get("raw", "")
        short = raw_text.strip().splitlines()
        short_text = short[0] if short else ""
        if len(short_text) > 160:
            short_text = short_text[:157] + "..."
        inline = comment.get("inline") or {}
        comments.append(
            {
                "id": comment.get("id"),
                "author": comment.get("user", {}).get("display_name"),
                "short": short_text,
                "file": inline.get("path"),
                "line": inline.get("to") or inline.get("line"),
            }
        )

    next_cursor = response.get("next")
    if next_cursor:
        next_cursor = _normalize_cursor(next_cursor)

    return comments, next_cursor


async def pr_overview(
    pr: str,
    repo: Optional[str] = None,
    verbosity: Verbosity = Verbosity.summary,
    ctx: Context | None = None,
) -> dict[str, Any]:
    """Return a composed digest of PR metadata, blockers, and recent activity."""

    ctx = ctx or get_context()
    workspace, repo_slug = _resolve_repo(repo, ctx)
    config = get_config_for_context(ctx)
    pr_id = str(pr).lstrip("#")

    details = await _fetch_pr(workspace, repo_slug, pr_id, config)
    statuses = await _fetch_pr_statuses(workspace, repo_slug, pr_id, config)
    diffstat_top, diffstat_cursor = await _fetch_pr_diffstat(workspace, repo_slug, pr_id, config)
    comments_recent, comments_cursor = await _fetch_recent_comments(workspace, repo_slug, pr_id, config)

    participants = details.get("participants", []) or []
    reviewer_count = sum(1 for participant in participants if participant.get("role") == "REVIEWER")
    approvals = sum(1 for participant in participants if participant.get("approved"))
    tasks = details.get("task_count") or {}
    tasks_open = tasks.get("open") or tasks.get("total") or 0

    failing_checks = sum(
        1
        for status in statuses
        if status.get("state") in {"FAILED", "ERROR", "STOPPED"}
    )

    merge_status = (details.get("merge_status") or "").lower()
    merge_conflicts = merge_status not in {"", "clean", "mergeable", "mergeable"}

    pr_summary = {
        "id": details.get("id"),
        "title": details.get("title", ""),
        "state": details.get("state"),
        "author": details.get("author", {}).get("display_name"),
        "updated": details.get("updated_on") or details.get("created_on"),
        "url": details.get("links", {}).get("html", {}).get("href"),
        "source": details.get("source", {}).get("branch", {}).get("name"),
        "destination": details.get("destination", {}).get("branch", {}).get("name"),
    }

    blockers = {
        "checks_failing": failing_checks,
        "required_approvals_left": max(reviewer_count - approvals, 0),
        "pending_tasks": tasks_open,
    }
    if merge_conflicts:
        blockers["merge_conflicts"] = True

    result: dict[str, Any] = {
        "pr": pr_summary,
        "blockers": blockers,
        "diffstat_top": diffstat_top,
        "comments_recent": comments_recent,
    }

    if comments_cursor or diffstat_cursor:
        cursor_payload = {}
        if comments_cursor:
            cursor_payload["comments_cursor"] = comments_cursor
        if diffstat_cursor:
            cursor_payload["files_cursor"] = diffstat_cursor
        result["next"] = cursor_payload

    if verbosity == "full":
        result["raw"] = {
            "details": details,
            "statuses": statuses,
        }

    return result


async def pr_review(
    pr: str,
    repo: Optional[str] = None,
    goal: Literal["quick", "thorough"] = "quick",
    policy: Literal["risk", "style", "both"] = "both",
    ctx: Context | None = None,
) -> dict[str, Any]:
    """Return a structured code review leveraging the overview digest."""

    overview = await pr_overview(pr=pr, repo=repo, verbosity=Verbosity.full, ctx=ctx)
    pr_info = overview.get("pr", {})
    blockers = overview.get("blockers", {})

    summary_parts = [
        f"PR #{pr_info.get('id')} · {pr_info.get('title', '').strip()}"
    ]

    if blockers.get("checks_failing"):
        summary_parts.append(f"{blockers['checks_failing']} failing checks")
    if blockers.get("required_approvals_left"):
        summary_parts.append(f"{blockers['required_approvals_left']} approvals needed")
    if blockers.get("pending_tasks"):
        summary_parts.append(f"{blockers['pending_tasks']} tasks open")
    if blockers.get("merge_conflicts"):
        summary_parts.append("merge conflicts detected")

    if len(summary_parts) == 1:
        summary_parts.append("No blockers detected")

    findings: list[dict[str, Any]] = []

    if blockers.get("checks_failing"):
        findings.append(
            {
                "severity": "high",
                "title": "CI checks failing",
                "why": "Bitbucket reports failed pipeline checks; please address before merging.",
                "suggest": "Open the pipeline logs to investigate failing steps.",
            }
        )
    if blockers.get("pending_tasks"):
        findings.append(
            {
                "severity": "med",
                "title": "Pending tasks",
                "why": "There are unresolved tasks attached to this PR.",
                "suggest": "Resolve or update outstanding tasks, or clarify remaining work.",
            }
        )
    if blockers.get("merge_conflicts"):
        findings.append(
            {
                "severity": "high",
                "title": "Merge conflicts",
                "why": "PR cannot be merged automatically due to conflicts.",
                "suggest": "Rebase or merge target branch and resolve conflicts.",
            }
        )

    summary = " · ".join(summary_parts)

    return {
        "summary": summary,
        "findings": findings,
        "suggested_inline_comments": [],
    }


def _pipeline_id(value: Any) -> str:
    return str(value).strip("{}") if value is not None else ""


async def _fetch_pipeline(
    workspace: str,
    repo_slug: str,
    pipeline_id: str,
    config: Config | None = None,
) -> dict[str, Any]:
    # The get pipeline endpoint accepts:
    # - Build number (e.g., "4636")
    # - UUID with braces (e.g., "{uuid-here}")
    # If it looks like a UUID without braces, we need to add them
    pipeline_id = str(pipeline_id).strip()

    # Check if it's a UUID format (has dashes in expected positions) but no braces
    if '-' in pipeline_id and not pipeline_id.startswith('{'):
        # Add braces for UUID format
        pipeline_id = f'{{{pipeline_id}}}'

    return await make_request(
        "GET",
        f"repositories/{workspace}/{repo_slug}/pipelines/{pipeline_id}",
        config=config,
    )


async def _list_failed_pipelines(
    workspace: str,
    repo_slug: str,
    limit: int,
    config: Config | None = None,
) -> list[dict[str, Any]]:
    response = await make_request(
        "GET",
        f"repositories/{workspace}/{repo_slug}/pipelines/",
        params={
            "pagelen": limit,
            "status": "FAILED",
            "sort": "-created_on",
        },
        config=config,
    )
    return response.get("values", []) or []


async def _list_pipeline_steps(
    workspace: str,
    repo_slug: str,
    pipeline_id: str,
    config: Config | None = None,
) -> list[dict[str, Any]]:
    response = await make_request(
        "GET",
        f"repositories/{workspace}/{repo_slug}/pipelines/{pipeline_id}/steps",
        config=config,
    )
    return response.get("values", []) or []


async def _fetch_step_logs(
    workspace: str,
    repo_slug: str,
    pipeline_id: str,
    step_uuid: str,
    config: Config | None = None,
) -> str:
    result = await make_request(
        "GET",
        f"repositories/{workspace}/{repo_slug}/pipelines/{pipeline_id}/steps/{step_uuid}/log",
        accept_type="application/octet-stream",
        config=config,
    )
    return result.get("content", "")


def _classify_error(log_text: str) -> tuple[str, list[str]]:
    lowered = log_text.lower()
    if "timeout" in lowered:
        kind = "timeout"
        hints = ["Review resource usage", "Consider increasing timeout or optimizing job"]
    elif "test" in lowered and "failed" in lowered:
        kind = "test_failure"
        hints = ["Run tests locally", "Check flaky test history"]
    elif "lint" in lowered or "eslint" in lowered:
        kind = "lint"
        hints = ["Run lint locally", "Check new files touched"]
    elif "error" in lowered or "traceback" in lowered:
        kind = "error"
        hints = ["Review stack trace", "Check recent commits affecting failing area"]
    else:
        kind = "unknown"
        hints = ["Inspect full logs for details"]
    return kind, hints


async def pipe_fail_summary(
    pipeline: Optional[str] = None,
    repo: Optional[str] = None,
    limit: int = 1,
    ctx: Context | None = None,
) -> dict[str, Any]:
    """Summarize failing pipeline steps with lightweight log excerpts."""

    ctx = ctx or get_context()
    workspace, repo_slug = _resolve_repo(repo, ctx)
    config = get_config_for_context(ctx)
    limit = max(1, min(limit, 3))

    pipelines: list[dict[str, Any]]
    if pipeline:
        # Pipeline can be either UUID (with/without braces) or build_number
        # The _fetch_pipeline handles both formats
        pipelines = [await _fetch_pipeline(workspace, repo_slug, pipeline, config)]
    else:
        pipelines = await _list_failed_pipelines(workspace, repo_slug, limit, config)
        if not pipelines:
            return {"items": []}

    summaries: list[dict[str, Any]] = []

    for pipeline_obj in pipelines[:limit]:
        # For steps endpoint, we need build_number, not UUID
        build_number = pipeline_obj.get("build_number")
        if not build_number:
            continue

        steps = await _list_pipeline_steps(workspace, repo_slug, str(build_number), config)
        failed_steps = [step for step in steps if step.get("state", {}).get("result", {}).get("name") == "FAILED"]
        if not failed_steps:
            continue

        step = failed_steps[0]
        step_uuid = step.get("uuid")
        if not step_uuid:
            continue
        try:
            logs = await _fetch_step_logs(
                workspace,
                repo_slug,
                str(build_number),
                step_uuid,
                config,
            )
        except Exception as exc:  # pragma: no cover - network failures
            logger.warning(f"Failed to fetch pipeline logs: {exc}")
            logs = ""

        lines = [line for line in logs.splitlines() if line.strip()]
        top_lines = (lines[-20:] if len(lines) > 20 else lines)[:20]

        error_kind, fix_hints = _classify_error("\n".join(top_lines))
        suspected_commit = (
            pipeline_obj.get("target", {})
            .get("commit", {})
            .get("hash")
        )

        summaries.append(
            {
                "id": str(build_number),
                "step": step.get("name") or "Unnamed step",
                "error_kind": error_kind,
                "top_lines": top_lines,
                "suspected_commit": suspected_commit,
                "fix_hints": fix_hints,
                "url": pipeline_obj.get("links", {}).get("html", {}).get("href"),
            }
        )

    return {"items": summaries}
