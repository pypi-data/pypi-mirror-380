#!/usr/bin/env python3
"""
Simple test script for FastMCP tools.
"""
import asyncio
import json
import sys
from typing import Any, Dict

# Add src to path for local imports
sys.path.insert(0, 'src')

from fastmcp import server


async def test_tools():
    """Test the add and minus tools."""
    print("Testing FastMCP tools...")
    print("=" * 40)
    
    # Test list_tools
    tools = await server.list_tools()()
    print(f"Available tools: {[tool.name for tool in tools]}")
    print()
    
    # Test add tool
    print("Testing add tool:")
    result = await server.call_tool()("add", {"a": 10, "b": 5})
    print(f"add(10, 5) = {result[0].text}")
    
    result = await server.call_tool()("add", {"a": -3, "b": 7})
    print(f"add(-3, 7) = {result[0].text}")
    print()
    
    # Test minus tool
    print("Testing minus tool:")
    result = await server.call_tool()("minus", {"a": 10, "b": 5})
    print(f"minus(10, 5) = {result[0].text}")
    
    result = await server.call_tool()("minus", {"a": -3, "b": 7})
    print(f"minus(-3, 7) = {result[0].text}")
    print()
    
    print("All tests completed successfully!")


if __name__ == "__main__":
    asyncio.run(test_tools())
