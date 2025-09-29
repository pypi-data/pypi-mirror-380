
"""
Bitbucket MCP Server
Main entry point that uses the composite pattern to combine tools and resources
Version: 2.1.0 - Now with CLI argument support for selective tool filtering
"""

from contextlib import asynccontextmanager

from fastmcp import FastMCP
from fastmcp.utilities.logging import get_logger

from src.modules.prompts import init as prompts_init
from src.modules.resources import init as resources_init

logger = get_logger(__name__)


@asynccontextmanager
async def resources_lifespan(app):
    """Lifespan context for registering resources and prompts."""
    logger.info("Initializing Bitbucket Resources Server...")
    await resources_init(app)
    logger.info("Bitbucket Resources initialized.")
    await prompts_init(app)
    logger.info("Bitbucket Prompts initialized.")
    yield


server = FastMCP(name="Bitbucket Resources Server", lifespan=resources_lifespan)

def main():
   server.run()


if __name__ == "__main__":
    main()
