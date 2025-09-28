"""Example MCP server using FastMCP."""

from fastmcp.server import FastMCP

# Create the FastMCP instance
mcp = FastMCP("My Server 🚀")

@mcp.tool("greet", description="Greet a user by name")
def greet(name: str) -> str:
    return f"Hello, {name}!"


def main():
    mcp.run()


# This allows the server to be run directly too
if __name__ == "__main__":
    mcp.run()
