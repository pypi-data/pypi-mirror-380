# ===== Main Registration Function =====


from fastmcp.resources import Resource
from fastmcp.utilities.logging import get_logger

from src.utils.config import get_config
from src.utils.workspace import ensure_workspace

from .iterators import register_pipeline_resources, register_pr_resources
from .resources import (
    get_branching_model,
    get_default_reviewers,
    get_open_prs,
    get_recent_pipelines,
    get_repository_branches,
    get_repository_info,
    get_workspace_members,
)

logger = get_logger(__name__)


async def init(mcp) -> None:
    """Register all resources."""

    logger.info("Registering Bitbucket resources...")

    config = get_config()

    try:
        workspace = (await ensure_workspace(config)).strip()
    except ValueError as exc:
        logger.warning(f"Skipping static resource registration: {exc}")
        return

    # Refresh config to ensure repo slug reflects any environment changes from discovery.
    config = get_config()
    workspace = workspace or config.workspace.strip()
    repo_slug = config.repo_slug.strip()

    if not repo_slug:
        logger.warning(
            "Skipping static resource registration: missing BITBUCKET_REPO"
        )
        return

    resource_specs = [
        (get_repository_info, "repo://{repo}/info"),
        (get_recent_pipelines, "pipelines://{repo}/recent"),
        (get_open_prs, "pull-requests://{repo}/open"),
        (get_workspace_members, "workspace://{workspace}/members"),
        (get_default_reviewers, "workspace://{workspace}/default-reviewers"),
        (get_repository_branches, "repo://{repo}/branches"),
        (get_branching_model, "repo://{repo}/branching-model"),
    ]

    resources_list = []
    for func, uri_template in resource_specs:
        try:
            uri = uri_template.format(repo=repo_slug, workspace=workspace)
        except KeyError:
            logger.error(f"Invalid URI template: {uri_template}")
            continue

        resources_list.append((func, uri))

    resources = [
        Resource.from_function(
            fn,
            uri,
            name=f"Resource for {uri}",
            title=f"Resource Information for {uri}",
            description=f"Details about the resource '{uri}'",
            mime_type="application/json",
        )
        for fn, uri in resources_list
    ]

    for resource in resources:
        mcp.add_resource(resource)

    # Register dynamic pipeline resources
    await register_pipeline_resources(mcp)

    # Register dynamic PR resources
    await register_pr_resources(mcp)
