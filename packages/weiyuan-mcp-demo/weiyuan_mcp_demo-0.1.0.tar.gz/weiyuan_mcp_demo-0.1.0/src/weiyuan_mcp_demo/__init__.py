# server.py
from mcp.server.fastmcp import FastMCP
# Create an MCP server instance
mcp = FastMCP("Demo Server", "A simple MCP server example.")

# Add an additional tool
@mcp.tool()
def add(x: int, y: int) -> int:
    """Add two numbers."""
    return x + y

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def main() -> None:
    mcp.settings.host = "0.0.0.0"
    mcp.run(transport='stdio')
    print("Hello from weiyuan-mcp-demo!")
