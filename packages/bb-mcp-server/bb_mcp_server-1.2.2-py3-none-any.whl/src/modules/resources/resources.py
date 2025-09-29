"""
Resource definitions for Bitbucket MCP Server
Contains all resource functions for accessing common Bitbucket data
"""

from fastmcp import Context
from fastmcp.utilities.logging import get_logger

from src.modules.tools import tools
from src.utils.api_client import make_request
from src.utils.config import get_config_for_context

logger = get_logger(__name__)

# ===== Static Resource Functions =====
# These are defined as standalone functions and registered via mcp.add_resource()

def _get_repo_context(ctx: Context) -> tuple:
    """Fetch config and ensure workspace/repo are available."""
    config = get_config_for_context(ctx)
    workspace = config.workspace.strip()
    repo_slug = config.repo_slug.strip()

    if not workspace or not repo_slug:
        raise ValueError(
            "Missing Bitbucket workspace/repo. Configure headers or environment variables."
        )

    return config, workspace, repo_slug


async def get_default_reviewers(ctx: Context) -> dict:
    try:
        config, workspace, repo_slug = _get_repo_context(ctx)
        await ctx.debug(f"Fetching default reviewers for {workspace}/{repo_slug}")
        default_reviewers = await make_request(
            "GET",
            f"repositories/{workspace}/{repo_slug}/default-reviewers",
            config=config,
        )

        reviewers = {}
        for reviewer in default_reviewers.get("values", []):
            account_id = reviewer.get("account_id", "")
            uuid = reviewer.get("uuid", "")
            reviewers[uuid] = {
                "username": reviewer.get("nickname", ""),
                "display_name": reviewer.get("display_name", ""),
                "account_id": account_id,
                "uuid": uuid,
                "source": "default_reviewer"
            }
        return reviewers

    except Exception as e:
        return {"error": str(e)}



async def get_repository_info(ctx: Context) -> dict:
    try:
        config, _, repo_slug = _get_repo_context(ctx)
    except ValueError as exc:
        return {"error": str(exc)}

    await ctx.debug(f"Fetching repository info for {repo_slug}")
    return await tools.repo_get(repo_slug, verbosity=tools.Verbosity.full, ctx=ctx)



async def get_recent_pipelines(ctx: Context) -> dict:
    try:
        config, workspace, repo_slug = _get_repo_context(ctx)
        await ctx.debug(f"Listing recent pipelines for {workspace}/{repo_slug}")
        pipelines = await make_request(
            "GET",
            f"repositories/{workspace}/{repo_slug}/pipelines",
            params={
                "pagelen": 10,
                "sort": "-created_on"
            },
            config=config,
        )
        return pipelines
    except Exception as e:
        return {"error": str(e)}

async def get_open_prs(ctx: Context) -> dict:
    try:
        config, _, repo_slug = _get_repo_context(ctx)
    except ValueError as exc:
        return {"error": str(exc)}

    await ctx.debug(f"Listing open PRs for {repo_slug}")
    return await tools.pr_list(
        repo_slug,
        state=tools.PRState.OPEN,
        verbosity=tools.Verbosity.full,
        limit=20,
        ctx=ctx,
    )



async def get_workspace_members(ctx: Context) -> dict:
    """Available PR reviewers in workspace"""
    try:
        config, workspace, _ = _get_repo_context(ctx)
        await ctx.debug(f"Fetching workspace members for {workspace}")
        members = await make_request(
            "GET",
            f"workspaces/{workspace}/members",
            config=config,
        )
        return members
    except Exception as e:
        return {"error": str(e)}


async def get_repository_branches(ctx: Context) -> dict:
    """All branches with latest commit info (max 50)"""
    try:
        config, workspace, repo_slug = _get_repo_context(ctx)
        await ctx.debug(f"Fetching branches for {workspace}/{repo_slug}")
        branches = await make_request(
            "GET",
            f"repositories/{workspace}/{repo_slug}/refs/branches",
            params={"pagelen": 50},
            config=config,
        )
        # Simplify branch data for easier consumption
        simplified = []
        for branch in branches.get("values", []):
            branch_data = {
                "name": branch.get("name", ""),
                "target_hash": branch.get("target", {}).get("hash", "")[:8],
                "last_commit_date": branch.get("target", {}).get("date"),
                "author": branch.get("target", {}).get("author", {}).get("user", {}).get("display_name")
            }
            # Only include branches with names
            if branch_data["name"]:
                simplified.append(branch_data)

        return {
            "branches": simplified,
            "count": len(simplified),
            "repository": f"{workspace}/{repo_slug}"
        }
    except Exception as e:
        return {"error": str(e)}


async def get_branching_model(ctx: Context) -> dict:
    """Branch strategy including default PR destination"""
    try:
        config, workspace, repo_slug = _get_repo_context(ctx)
        await ctx.debug(f"Fetching branching model for {workspace}/{repo_slug}")
        model = await make_request(
            "GET",
            f"repositories/{workspace}/{repo_slug}/branching-model",
            config=config,
        )

        # Simplify the response for easier consumption
        simplified = {
            "development_branch": None,
            "production_branch": None,
            "branch_prefixes": {},
            "default_pr_destination": None
        }

        if "development" in model and model["development"]:
            simplified["development_branch"] = model["development"].get("name")
            simplified["default_pr_destination"] = model["development"].get("name")

        if "production" in model and model["production"]:
            simplified["production_branch"] = model["production"].get("name")
            if not simplified["default_pr_destination"]:
                simplified["default_pr_destination"] = model["production"].get("name")

        if "branch_types" in model:
            for branch_type in model["branch_types"]:
                kind = branch_type.get("kind", "")
                prefix = branch_type.get("prefix", "")
                if kind and prefix:
                    simplified["branch_prefixes"][kind] = prefix

        return simplified

    except Exception as e:
        return {
            "error": str(e),
            "development_branch": "develop",
            "production_branch": "master",
            "default_pr_destination": "develop"
        }
