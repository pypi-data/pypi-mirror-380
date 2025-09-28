# MCP Agents - Example FastMCP Server

A simple Model Context Protocol (MCP) server built with FastMCP that demonstrates basic tool implementation.

## Features

- **greet**: Greet a user by name

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

To start the MCP agents server:

```bash
just run
```

### Using with MCP Clients

You can use this server with any MCP-compatible client. The configuration depends on how you want to run the server:

#### Option 1: Local Development (using source code)

For development or when running from a local clone:

```json
{
  "mcpServers": {
    "mcp-agents": {
      "command": "uv",
      "args": ["run", "mcp-agents"],
      "cwd": "/Users/means/repository/mcp-agents",
      "env": {}
    }
  }
}
```

#### Option 2: PyPI Installation (recommended for end users)

Once published to PyPI, users can use this simpler configuration:

```json
{
  "mcpServers": {
    "mcp-agents": {
      "command": "uvx",
      "args": ["amajakai14_mcp-agents"]
    }
  }
}
```

Alternative with `pipx`:
```json
{
  "mcpServers": {
    "mcp-agents": {
      "command": "pipx",
      "args": ["run", "amajakai14_mcp-agents"]
    }
  }
}
```

#### Option 3: Version Pinning

To pin to a specific version:

```json
{
  "mcpServers": {
    "mcp-agents": {
      "command": "uvx",
      "args": ["amajakai14_mcp-agents==0.1.0"]
    }
  }
}
```

#### For Claude Desktop

Add any of the above configurations to your Claude Desktop config file:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

### Testing the Tools

Run the test script to verify the tools work correctly:

```bash
just test
```

## Available Tools

### greet
Greets a user by name.

**Parameters:**
- `name` (string): The name of the person to greet

**Returns:**
A friendly greeting message.

**Example:**
```json
{
  "name": "greet",
  "arguments": {
    "name": "Alice"
  }
}
```

**Response:**
```
"Hello, Alice!"
```

## Development

### Available Just Commands

- `just build` - Install dependencies and sync the project
- `just run` - Start the MCP agents server
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
│   └── agents/
│       └── __init__.py          # Main MCP server implementation
├── pyproject.toml               # Project configuration and dependencies
├── justfile                     # Task runner configuration
├── mcp_config.json             # MCP client configuration example
├── test_tools.py               # Simple test script
└── README.md                   # This file
```

### Adding New Tools

To add new tools using FastMCP:

1. Add a new function with the `@mcp.tool()` decorator:
   ```python
   @mcp.tool("tool_name", description="Description of what the tool does")
   def tool_name(param1: type, param2: type) -> return_type:
       # Tool implementation
       return result
   ```

2. Update the README with documentation for the new tool

### Running Tests

```bash
just test
```

## License

MIT License
