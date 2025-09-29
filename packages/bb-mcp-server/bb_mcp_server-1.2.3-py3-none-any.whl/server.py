
"""
Bitbucket MCP Server
HTTP-only FastMCP entry point aligned with framework run() patterns.
"""
from __future__ import annotations

import argparse
import os
from typing import Sequence

from fastmcp import FastMCP
from fastmcp.utilities.logging import configure_logging, get_logger

configure_logging(level=os.getenv("MCP_LOG_LEVEL", "DEBUG"))
logger = get_logger(__name__)

from src.modules.middleware import BearerAuthMiddleware
from src.utils.config import SERVER_INSTRUCTIONS, SERVER_NAME
from src.utils.security import get_security_warnings


def _import_child_servers():
    """Import tool and resource servers with package/module fallback."""
    try:  # Package installation path
        from .resources_server import server as resources_server  # type: ignore[import]
        from .tools_server import server as tools_server  # type: ignore[import]
    except ImportError:  # Local development path
        from resources_server import server as resources_server  # type: ignore[import]
        from tools_server import server as tools_server  # type: ignore[import]

    return resources_server, tools_server


def create_server() -> FastMCP:
    """Construct the FastMCP server instance with middleware and mounts."""
    server_instance = FastMCP(
        SERVER_NAME,
        instructions=SERVER_INSTRUCTIONS,
    )

    server_instance.add_middleware(BearerAuthMiddleware())
    logger.info("Authentication middleware enabled for HTTP transport")

    resources_server, tools_server = _import_child_servers()

    if os.getenv("NO_TOOLS") is None:
        logger.debug("Mounting tools server")
        server_instance.mount(tools_server)
    else:
        logger.info("Tools server disabled via NO_TOOLS environment flag")

    server_instance.mount(resources_server)
    return server_instance


server = create_server()


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the Bitbucket FastMCP server.")
    parser.add_argument("--host", default=None, help="HTTP host to bind (env FASTMCP_HOST).")
    parser.add_argument("--port", type=int, default=None, help="HTTP port to bind (env FASTMCP_PORT/PORT).")
    parser.add_argument(
        "--transport",
        default="http",
        help="FastMCP transport to use (http only).",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> None:
    args = _parse_args(argv)

    if args.transport.lower() != "http":
        raise RuntimeError("This server only supports the HTTP transport. Use --transport http.")

    port = args.port or int(os.getenv("FASTMCP_PORT", os.getenv("PORT", "8000")))
    host = args.host or os.getenv("FASTMCP_HOST", "localhost")

    for warning in get_security_warnings("http"):
        logger.warning(warning)

    logger.info(f"Starting HTTP server on {host}:{port}")
    server.run(transport="http", host=host, port=port)


if __name__ == "__main__":
    main()
    
