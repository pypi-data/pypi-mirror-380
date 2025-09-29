from contextlib import asynccontextmanager

from fastmcp import FastMCP
from fastmcp.utilities.logging import get_logger

logger = get_logger(__name__)

@asynccontextmanager
async def default_lifespan(app):
    await add_tools(app)
    yield

server = FastMCP("Proxy Server", lifespan=default_lifespan)


# Create a proxy directly from a config dictionary
config = {
    "mcpServers": {
        "chrome-devtools-mcp": {
            "args": [
                "chrome-devtools-mcp",
            ],
            "command": "npx"
        }
    }
}

# Create a proxy to the configured server (auto-creates ProxyClient)
proxy = FastMCP.as_proxy(config, name="Config-Based Proxy")
    
tools_list = [
    ["list_console_messages", True],
    ["emulate_cpu", False],
    ["emulate_network", False],
    ["click", False],
    ["drag", False],
    ["fill", False],
    ["fill_form", False],
    ["hover", False],
    ["upload_file", False],
    ["get_network_request", True],
    ["list_network_requests", True],
    ["close_page", True],
    ["handle_dialog", False],
    ["list_pages", True],
    ["navigate_page", True],
    ["navigate_page_history", True],
    ["new_page", True],
    ["resize_page", False],
    ["select_page", False],
    ["performance_analyze_insight", False],
    ["performance_start_trace", False],
    ["performance_stop_trace", False],
    ["take_screenshot", True],
    ["evaluate_script", False],
    ["take_snapshot", True],
    ["wait_for", True]
]

# Add only the tools we want to expose
async def add_tools(app):
    for tool in tools_list:
        mirrored_tool = await proxy.get_tool(tool[0])
        logger.info(f"Adding tool: {mirrored_tool.name}, enabled: {tool[1]}")
        local_tool = mirrored_tool.copy()
        server.add_tool(local_tool)
        local_tool.enabled = tool[1]
        
def main():
    server.run()
        
# Run the proxy with stdio transport for local access
if __name__ == "__main__":
    main()

args = [
    "--tool",
    "list_console_messages",
    "--tool", 
    "list_network_requests",
    "--tool", 
    "get_network_request",
    "--tool", 
    "close_page",
    "--tool", 
    "list_pages",
    "--tool", 
    "navigate_page",
    "--tool", 
    "navigate_page_history",
    "--tool", 
    "new_page",
    "--tool", 
    "take_screenshot",
    "--tool", 
    "take_snapshot",
    "--tool", 
    "wait_for"
]