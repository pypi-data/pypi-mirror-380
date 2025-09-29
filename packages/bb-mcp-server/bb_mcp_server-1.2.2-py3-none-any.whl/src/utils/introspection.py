"""
Server Introspection Utilities
Provides tools for inspecting and analyzing composed servers
"""

from typing import Dict, List, Any, Optional
from fastmcp import FastMCP
from fastmcp.utilities.logging import get_logger

logger = get_logger(__name__)


class ServerIntrospector:
    """Utilities for inspecting MCP server composition."""

    def __init__(self, server: Any):
        """Initialize with a server instance."""
        self.server = server

    def get_server_info(self) -> Dict[str, Any]:
        """
        Get comprehensive information about the server.

        Returns:
            Dictionary with server metadata and capabilities
        """
        info = {
            'name': getattr(self.server, 'name', 'unknown'),
            'type': type(self.server).__name__,
            'has_lifespan': hasattr(self.server, 'lifespan'),
            'capabilities': self._get_capabilities()
        }

        # Add enhanced server specific info
        if hasattr(self.server, 'mounted_servers'):
            info['mounted_servers'] = list(self.server.mounted_servers.keys())
            info['mount_config'] = self.server.mount_config

        return info

    def _get_capabilities(self) -> Dict[str, int]:
        """Get counts of server capabilities."""
        capabilities = {
            'tools': 0,
            'resources': 0,
            'prompts': 0
        }

        # Count registered components
        if hasattr(self.server, '_tools'):
            capabilities['tools'] = len(self.server._tools)
        if hasattr(self.server, '_resources'):
            capabilities['resources'] = len(self.server._resources)
        if hasattr(self.server, '_prompts'):
            capabilities['prompts'] = len(self.server._prompts)

        return capabilities

    def list_tools(self, include_disabled: bool = True) -> List[Dict[str, Any]]:
        """
        List all tools with their metadata.

        Args:
            include_disabled: Whether to include disabled tools

        Returns:
            List of tool information dictionaries
        """
        tools = []

        if not hasattr(self.server, '_tools'):
            return tools

        for tool_name, tool_func in self.server._tools.items():
            tool_info = {
                'name': tool_name,
                'description': tool_func.__doc__ or '',
                'disabled': False
            }

            # Check if tool is disabled
            if hasattr(tool_func, '_disabled'):
                tool_info['disabled'] = tool_func._disabled
                if not include_disabled and tool_info['disabled']:
                    continue

            # Get annotations if available
            if hasattr(tool_func, '_annotations'):
                tool_info['annotations'] = tool_func._annotations

            tools.append(tool_info)

        return sorted(tools, key=lambda x: x['name'])

    def list_resources(self) -> List[Dict[str, Any]]:
        """
        List all resources with their metadata.

        Returns:
            List of resource information dictionaries
        """
        resources = []

        if not hasattr(self.server, '_resources'):
            return resources

        for uri, resource_func in self.server._resources.items():
            resource_info = {
                'uri': uri,
                'description': resource_func.__doc__ or '',
                'is_template': '{' in uri  # Simple check for URI templates
            }

            resources.append(resource_info)

        return sorted(resources, key=lambda x: x['uri'])

    def list_prompts(self) -> List[Dict[str, Any]]:
        """
        List all prompts with their metadata.

        Returns:
            List of prompt information dictionaries
        """
        prompts = []

        if not hasattr(self.server, '_prompts'):
            return prompts

        for prompt_name, prompt_func in self.server._prompts.items():
            prompt_info = {
                'name': prompt_name,
                'description': prompt_func.__doc__ or ''
            }

            prompts.append(prompt_info)

        return sorted(prompts, key=lambda x: x['name'])

    def get_tool_categories(self) -> Dict[str, List[str]]:
        """
        Group tools by category.

        Returns:
            Dictionary mapping categories to tool names
        """
        categories = {}

        for tool in self.list_tools():
            if 'annotations' in tool and 'category' in tool['annotations']:
                category = tool['annotations']['category']
                if category not in categories:
                    categories[category] = []
                categories[category].append(tool['name'])

        return categories

    def get_statistics(self) -> Dict[str, Any]:
        """
        Get comprehensive statistics about the server.

        Returns:
            Dictionary with various statistics
        """
        tools = self.list_tools()
        resources = self.list_resources()
        prompts = self.list_prompts()

        stats = {
            'total_tools': len(tools),
            'enabled_tools': len([t for t in tools if not t.get('disabled', False)]),
            'disabled_tools': len([t for t in tools if t.get('disabled', False)]),
            'total_resources': len(resources),
            'static_resources': len([r for r in resources if not r.get('is_template', False)]),
            'template_resources': len([r for r in resources if r.get('is_template', False)]),
            'total_prompts': len(prompts),
            'tool_categories': self.get_tool_categories()
        }

        return stats

    def generate_report(self) -> str:
        """
        Generate a human-readable report about the server.

        Returns:
            Formatted report string
        """
        info = self.get_server_info()
        stats = self.get_statistics()

        report = []
        report.append(f"=== Server Introspection Report ===")
        report.append(f"\nServer: {info['name']}")
        report.append(f"Type: {info['type']}")

        if 'mounted_servers' in info:
            report.append(f"\nMounted Servers: {', '.join(info['mounted_servers'])}")

        report.append(f"\n=== Statistics ===")
        report.append(f"Tools: {stats['total_tools']} total ({stats['enabled_tools']} enabled, {stats['disabled_tools']} disabled)")
        report.append(f"Resources: {stats['total_resources']} total ({stats['static_resources']} static, {stats['template_resources']} templates)")
        report.append(f"Prompts: {stats['total_prompts']} total")

        if stats['tool_categories']:
            report.append(f"\n=== Tool Categories ===")
            for category, tool_names in sorted(stats['tool_categories'].items()):
                report.append(f"  {category}: {len(tool_names)} tools")

        return '\n'.join(report)


def introspect_server(server: Any) -> ServerIntrospector:
    """
    Create an introspector for a server.

    Args:
        server: The server to introspect

    Returns:
        ServerIntrospector instance
    """
    return ServerIntrospector(server)


def compare_servers(server1: Any, server2: Any) -> Dict[str, Any]:
    """
    Compare two servers to identify differences.

    Args:
        server1: First server
        server2: Second server

    Returns:
        Dictionary with comparison results
    """
    intro1 = ServerIntrospector(server1)
    intro2 = ServerIntrospector(server2)

    tools1 = set(t['name'] for t in intro1.list_tools())
    tools2 = set(t['name'] for t in intro2.list_tools())

    resources1 = set(r['uri'] for r in intro1.list_resources())
    resources2 = set(r['uri'] for r in intro2.list_resources())

    comparison = {
        'server1_name': intro1.get_server_info()['name'],
        'server2_name': intro2.get_server_info()['name'],
        'tools': {
            'only_in_server1': list(tools1 - tools2),
            'only_in_server2': list(tools2 - tools1),
            'common': list(tools1 & tools2)
        },
        'resources': {
            'only_in_server1': list(resources1 - resources2),
            'only_in_server2': list(resources2 - resources1),
            'common': list(resources1 & resources2)
        }
    }

    return comparison