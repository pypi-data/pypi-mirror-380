
from fastmcp import Context

from src.utils.api_client import make_request
from src.utils.config import get_config_for_context


def _get_repo_context(ctx: Context) -> tuple[str, str]:
    """Get current workspace and repo from configuration."""
    config = get_config_for_context(ctx)
    workspace = config.workspace.strip()
    repo_slug = config.repo_slug.strip()

    if not workspace or not repo_slug:
        raise ValueError(
            "Missing Bitbucket workspace/repo. Configure headers or environment variables."
        )

    return workspace, repo_slug


async def commit_push_and_create_pr(ctx: Context) -> str:
    try:
        workspace, repo_slug = _get_repo_context(ctx)
    except ValueError as exc:
        return str(exc)

    config = get_config_for_context(ctx)
    await ctx.debug(f"Prompt: recommend reviewers for {workspace}/{repo_slug}")
    reviewers = await make_request(
        "GET",
        f"repositories/{workspace}/{repo_slug}/default-reviewers",
        accept_type="application/json",
        config=config,
    )
    user = await make_request("GET", "user", accept_type="application/json", config=config)
    reviewers["values"] = [
        r for r in reviewers["values"] if r["uuid"] != user["uuid"]
    ]
    if not reviewers["values"]:
        return (
            "Commit all changes, push to remote, and create a pull request in the "
            "Bitbucket UI (no direct tooling exposed)."
        )
    reviewers["values"] = [
        f"{r['display_name']} ({r['uuid']})" for r in reviewers["values"]
    ]
    return (
        "Commit all changes, push to remote, and create a pull request in Bitbucket. "
        f"Suggested reviewers: {reviewers['values']}."
    )


async def create_markdown_from_latest_failed_pipeline(ctx: Context) -> str:
    try:
        workspace, repo_slug = _get_repo_context(ctx)
    except ValueError as exc:
        return str(exc)

    config = get_config_for_context(ctx)
    await ctx.debug("Prompt: fetching latest failed pipeline")
    pipeline = await make_request(
        "GET",
        f"repositories/{workspace}/{repo_slug}/pipelines/?sort=-created_on&pagelen=1&status=FAILED",
        accept_type="application/json",
        config=config,
    )
    return (
        "Call pipe.fail.summary to summarise the latest failed pipeline, then "
        f"create a markdown report from the returned items: {pipeline}"
    )
