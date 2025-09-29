"""Middleware module for Bitbucket MCP Server"""

from .auth import BearerAuthMiddleware

__all__ = ["BearerAuthMiddleware"]