# FastMCP - Simple Math Tools

A simple Model Context Protocol (MCP) server that provides basic mathematical operations as tools.

## Features

- **add**: Add two numbers together
- **minus**: Subtract the second number from the first number

## Installation

This project uses `uv` for package management and `just` for task running. Make sure you have both installed:

```bash
# Install uv if you don't have it
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install just if you don't have it
# On macOS with Homebrew:
brew install just
# Or with cargo:
cargo install just
```

Then build the project:

```bash
just build
```

## Usage

### Running the MCP Server

To start the FastMCP server:

```bash
just run
```

### Using with MCP Clients

You can use this server with any MCP-compatible client. Here's an example configuration for `mcp_config.json`:

```json
{
  "mcpServers": {
    "fastmcp": {
      "command": "uv",
      "args": ["run", "fastmcp"],
      "cwd": "/path/to/mcp-agents"
    }
  }
}
```

### Testing the Tools

Run the test script to verify the tools work correctly:

```bash
just test
```

## Available Tools

### add
Adds two numbers together.

**Parameters:**
- `a` (number): First number
- `b` (number): Second number

**Example:**
```json
{
  "name": "add",
  "arguments": {
    "a": 10,
    "b": 5
  }
}
```

### minus
Subtracts the second number from the first number.

**Parameters:**
- `a` (number): Number to subtract from
- `b` (number): Number to subtract

**Example:**
```json
{
  "name": "minus",
  "arguments": {
    "a": 10,
    "b": 3
  }
}
```

## Development

### Available Just Commands

- `just build` - Install dependencies and sync the project
- `just run` - Start the FastMCP server
- `just test` - Run the test script
- `just format` - Format code with black and isort
- `just typecheck` - Run type checking with mypy
- `just dev` - Install development dependencies
- `just dist` - Build distribution packages
- `just clean` - Clean build artifacts
- `just publish` - Publish to PyPI (used in CI)

### Project Structure

```
mcp-agents/
├── src/
│   └── fastmcp/
│       └── __init__.py          # Main MCP server implementation
├── pyproject.toml               # Project configuration and dependencies
├── justfile                     # Task runner configuration
├── mcp_config.json             # MCP client configuration example
├── test_tools.py               # Simple test script
└── README.md                   # This file
```

### Adding New Tools

To add new tools:

1. Add the tool definition to the `handle_list_tools()` function
2. Add the tool implementation to the `handle_call_tool()` function
3. Update the README with documentation for the new tool

### Running Tests

```bash
just test
```

## License

MIT License
