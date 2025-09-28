# Build the project
build:
    uv sync

# Run the FastMCP server
run:
    uv run mcp-agents

# Run tests
test:
    uv run python test_tools.py

# Format code
format:
    uv run black src/
    uv run isort src/

# Type check
typecheck:
    uv run mypy src/

# Clean build artifacts
clean:
    rm -rf dist/
    rm -rf build/
    rm -rf *.egg-info/

# Install development dependencies
dev:
    uv sync --extra dev

# Build distribution packages
dist:
    uv build

# Publish to PyPI (for CI)
publish:
    uv publish dist/*
