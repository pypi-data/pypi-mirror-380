"""
FastMCP - A simple Model Context Protocol server with basic math tools.
"""
from fastmcp.server import FastMCP

# Import tools to register them
from fastmcp.tools import math


def main():
    """Main entry point for the FastMCP server."""
    # Run the server with registered tools
    math.mcp.run()


if __name__ == "__main__":
    main()
