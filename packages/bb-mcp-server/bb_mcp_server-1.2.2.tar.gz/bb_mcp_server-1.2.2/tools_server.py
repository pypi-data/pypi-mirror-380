
"""
Bitbucket MCP Server
Main entry point that uses the composite pattern to combine tools and resources
Version: 2.1.0 - Now with CLI argument support for selective tool filtering
"""

import os
from contextlib import asynccontextmanager

from fastmcp import FastMCP
from fastmcp.utilities.logging import get_logger

from src.modules import tools

logger = get_logger(__name__)

@asynccontextmanager
async def main_server_lifespan(app):
    """Lifespan context for registering tools and resources."""

    # Get allowed tools from environment variable (client configuration)
    # Client can set this in their MCP config file via env: {"ALLOWED_TOOLS": "tool1,tool2,tool3"}
    allowed_tools_str = os.getenv("ALLOWED_TOOLS", "")

    if allowed_tools_str:
        # Parse comma-separated list of tool names
        allowed_tools = [tool.strip() for tool in allowed_tools_str.split(",") if tool.strip()]
        logger.info(f"Using client-specified allowed tools: {allowed_tools}")
    else:
        # Default: enable all tools
        allowed_tools = []
        logger.info("No tool restrictions specified - all tools will be enabled")

    await tools.init(app, allowed_tools=allowed_tools)

    yield


server = FastMCP("Tools Server", lifespan=main_server_lifespan)

def main():
    server.run()

if __name__ == "__main__":
    main()