# ===== Dynamic Iterator Functions =====
# These use the decorator pattern since they dynamically create resources

from fastmcp.resources import Resource
from fastmcp.utilities.logging import get_logger

from src.utils.api_client import make_request
from src.utils.config import get_config

logger = get_logger(__name__)


def _get_repo_context():
    """Get workspace and repo from the active configuration."""
    config = get_config()
    workspace = config.workspace.strip()
    repo_slug = config.repo_slug.strip()

    if not workspace or not repo_slug:
        raise ValueError(
            "Missing Bitbucket workspace/repo. Configure headers or environment variables."
        )

    return workspace, repo_slug


async def register_pipeline_resources(mcp) -> None:
    """
    Dynamically register recent pipeline runs as individual resources.
    Uses Resource.from_function for lazy loading of pipeline details.
    """
    logger.info("Fetching recent pipelines for resource registration...")

    try:
        # Fetch recent pipeline runs with minimal fields for registration
        workspace, repo_slug = _get_repo_context()

        pipelines_response = await make_request(
            "GET",
            f"repositories/{workspace}/{repo_slug}/pipelines/",
            params={
                "pagelen": 15,
                "sort": "-created_on",
                "fields": (
                    "values.uuid,values.build_number,values.target,values.state.name,"
                    "values.created_on"
                ),
            },
        )
        pipelines = pipelines_response.get("values", [])

        for pipeline in pipelines:
            pipeline_uuid = pipeline.get("uuid")
            build_number = pipeline.get("build_number")
            target = pipeline.get("target", {})
            destination_branch = target.get("destination", "unknown") if target else "unknown"
            source_branch = target.get("source", "unknown") if target else "unknown"
            state = pipeline.get("state", {}).get("name", "UNKNOWN")
            created_on = pipeline.get("created_on", "Unknown")[:19]

            if not pipeline_uuid or not build_number:
                continue

            # Create resource using from_function with a lambda that captures pipeline_uuid
            # Note: The Bitbucket API requires UUID with braces for the pipeline endpoint
            resource = Resource.from_function(
                fn=lambda uuid=pipeline_uuid, _workspace=workspace, _repo=repo_slug: make_request(
                    "GET",
                    f"repositories/{_workspace}/{_repo}/pipelines/{uuid}"
                ),
                uri=f"pipelines://runs/#{build_number}",
                name=f"Pipeline #{build_number} [{state}]",
                title=f"Pipeline #{build_number} - {source_branch} → {destination_branch}",
                description=(
                    f"Pipeline #{build_number} ({state}) - "
                    f"Created: {created_on}"
                ),
                mime_type="application/json"
            )

            mcp.add_resource(resource)
            logger.info(f"Registered resource for pipeline #{build_number} [{state}]")

        logger.info(f"Successfully registered {len(pipelines)} pipeline resources")

    except Exception as e:
        logger.error(f"Failed to register pipeline resources: {str(e)}")

async def register_pr_resources(mcp) -> None:
    """
    Dynamically register recent PRs created by the current user as individual resources.
    Uses Resource.from_function for lazy loading of PR details.
    """
    logger.info("Fetching recent PRs for resource registration...")

    try:
        # First get the current user to filter PRs
        workspace, repo_slug = _get_repo_context()

        current_user = await make_request("GET", "user")
        user_uuid = current_user.get("uuid")

        if not user_uuid:
            logger.warning("Could not get current user UUID, skipping PR resource registration")
            return

        # Fetch PRs with minimal fields for registration
        prs_response = await make_request(
            "GET",
            f"repositories/{workspace}/{repo_slug}/pullrequests",
            params={
                "q": f'author.uuid="{user_uuid}"',
                "sort": "-created_on",
                "pagelen": 15,
                "fields": (
                    "values.id,values.title,values.state,values.source.branch.name,"
                    "values.destination.branch.name,values.created_on"
                ),
            },
        )

        prs = prs_response.get("values", [])

        for pr in prs:
            pr_id = pr.get("id")
            if not pr_id:
                continue

            pr_title = pr.get("title", "Untitled")
            pr_state = pr.get("state", "UNKNOWN")
            source_branch = pr.get("source", {}).get("branch", {}).get("name", "unknown")
            destination_branch = pr.get("destination", {}).get("branch", {}).get("name", "unknown")
            created_on = pr.get("created_on", "Unknown")[:19]

            # Create resource using from_function with a lambda that captures pr_id
            resource = Resource.from_function(
                fn=lambda pr_id=pr_id, _workspace=workspace, _repo=repo_slug: make_request(
                    "GET",
                    f"repositories/{_workspace}/{_repo}/pullrequests/{pr_id}"
                ),
                uri=f"pull-requests://#{pr_id}",
                name=f"PR #{pr_id} [{pr_state}]",
                title=f"PR #{pr_id} - {source_branch} → {destination_branch}",
                description=(
                    f"Pull request #{pr_id}: {pr_title} "
                    f"({pr_state}) - Created: {created_on}"
                ),
                mime_type="application/json"
            )

            mcp.add_resource(resource)
            logger.info(f"Registered resource for PR #{pr_id} [{pr_state}]")

        logger.info(f"Successfully registered {len(prs)} PR resources")

    except Exception as e:
        logger.error(f"Failed to register PR resources: {str(e)}")
