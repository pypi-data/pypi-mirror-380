from fastmcp.prompts import Prompt

from .prompts import (commit_push_and_create_pr,
                      create_markdown_from_latest_failed_pipeline)


async def init(mcp):
    """Register all prompts."""
    prompts = [
        [commit_push_and_create_pr,"Generates a prompt to commit all changes, push to remote, and create a PR. Includes default reviewers"],
        [create_markdown_from_latest_failed_pipeline,"Generates a prompt based on data that needs to be fetched."],
    ]
    for prompt in prompts:
        mcp.add_prompt(Prompt.from_function(prompt[0], description=prompt[1]))