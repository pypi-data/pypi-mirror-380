# Ollama Web Search MCP Service

A MCP (Model Context Protocol) service for performing web searches using Ollama.

## Features

- Perform web searches using Ollama's search capabilities
- Format search results for easy consumption
- Official MCP Python SDK implementation
- Environment-based configuration
- Comprehensive error handling
- Stdio-based communication interface

## Installation & Usage

### Option 1: Direct execution with uvx (Recommended)

Install and run directly using uvx:

```bash
uvx ollama-websearch-mcp
```

This will automatically install the package and its dependencies, then start the MCP server.

### Option 2: Local development

For local development, clone the repository and install dependencies:

```bash
git clone https://github.com/huangxinping/ollama-websearch-mcp.git
cd ollama-websearch-mcp
uv sync
```

### Local usage commands

**Run as MCP Server (for development)**:
```bash
python mcp_service.py
```

**Build Package**:
```bash
uv build
```

## MCP Interface

### Tools

1. **search**
   - Description: Perform a web search using Ollama
   - Parameters:
     - `query` (string): The search query
     - `max_results` (integer, optional): Maximum number of results to return (default: 3, range: 1-10)

### Example Output

Search result format:
```
1. Example Title
   URL: https://example.com
   Content: Example content from the search result...

2. Another Title
   URL: https://another-example.com
   Content: Another example content...
```

## Project Structure

```
ollama-websearch-mcp/
├── mcp_service.py             # MCP service main program
├── README.md                  # Project documentation
├── .env                       # Environment variables
├── .gitignore                 # Git ignore file
├── pyproject.toml             # Project configuration file
├── setup.py                   # Package setup file
└── uv.lock                    # Dependency lock file
```

## Tech Stack

- **Python 3.12+**: Programming language
- **MCP**: Model Context Protocol framework
- **Ollama**: AI model API for web search
- **python-dotenv**: Environment variable management
- **uv**: Python package manager

## Development Standards

- Use uv native commands for package management
- Follow Python PEP 8 coding standards
- Include type hints and docstrings
- Complete error handling and logging

## Publishing to PyPI

To publish the package to PyPI, follow these steps:

1. Install development dependencies:
   ```bash
   uv sync --group dev
   ```

2. Build the package:
   ```bash
   uv build
   ```

3. Check the built package:
   ```bash
   uv run twine check dist/*
   ```

4. Upload to PyPI:
   ```bash
   uv run twine upload dist/*
   ```

Make sure you have your PyPI credentials configured before uploading.

## AI IDE/CLI Configuration

### Claude Code (CLI)

Add to your MCP configuration:

```json
{
  "mcpServers": {
    "ollama-websearch": {
      "command": "uvx",
      "args": ["ollama-websearch-mcp"],
      "env": {
        "OLLAMA_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

### Cursor IDE

Add to your `.cursorrules` or MCP settings:

```json
{
  "mcp": {
    "servers": {
      "ollama-websearch": {
        "command": "uvx",
        "args": ["ollama-websearch-mcp"],
        "env": {
           "OLLAMA_API_KEY": "your_api_key_here"
        }
      }
    }
  }
}
```

### Windsurf IDE

Add to your Windsurf MCP configuration:

```json
{
  "mcpServers": {
    "ollama-websearch": {
      "command": "uvx",
      "args": ["ollama-websearch-mcp"],
        "env": {
           "OLLAMA_API_KEY": "your_api_key_here"
        }
    }
  }
}
```

### VS Code with Continue Extension

Add to your `continue` configuration:

```json
{
  "mcp": {
    "servers": {
      "ollama-websearch": {
        "command": "uvx",
        "args": ["ollama-websearch-mcp"],
        "env": {
           "OLLAMA_API_KEY": "your_api_key_here"
        }
      }
    }
  }
}
```

### Other MCP-Compatible Tools

For any MCP-compatible client, use:

```bash
# Command
uvx ollama-websearch-mcp

# Or with Python path
python -m mcp_service
```

## License

MIT License