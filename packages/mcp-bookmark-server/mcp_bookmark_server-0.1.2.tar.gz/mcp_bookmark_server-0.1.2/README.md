# MCP Bookmark Server

mcp-name: io.github.pree-dew/mcp-bookmark

A Model Context Protocol (MCP) server that enables AI assistants to save and search bookmarks using OpenAI's RAG capabilities. Store URLs with metadata and perform intelligent searches across your bookmark collection.

## Features

- **Save Bookmarks**: Store URLs with titles and descriptions
- **Smart Search**: Search across bookmark titles and descriptions using semantic search
- **AI-Powered**: Integration with OpenAI for intelligent bookmark management and categorization
- **Multi-Platform**: Easy integration across multiple MCP-compatible platforms

## Installation

```bash
pip install mcp-bookmark-server
```

## Configuration for MCP Hosts

### Claude Desktop

Add to your `claude_desktop_config.json`:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "bookmark": {
      "command": "/usr/local/bin/uvx",
      "args": [
        "--from",
        "git+https://github.com/pree-dew/mcp-bookmark.git",
        "mcp-bookmark-server"
      ],
      "env": {
        "OPENAI_API_KEY": "your-openai-api-key-here"
      }
    }
  }
}
```

### Cursor IDE

Add to your MCP settings in `.cursor/mcp_config.json`:

```json
{
  "mcpServers": {
    "bookmark": {
      "command": "/usr/local/bin/uvx",
      "args": [
        "--from",
        "git+https://github.com/pree-dew/mcp-bookmark.git",
        "mcp-bookmark-server"
      ],
      "env": {
        "OPENAI_API_KEY": "your-openai-api-key-here"
      }
    }
  }
}
```

### Windsurf IDE

Add to your `windsurf_config.json`:

```json
{
  "mcpServers": {
    "bookmark": {
      "command": "/usr/local/bin/uvx",
      "args": [
        "--from",
        "git+https://github.com/pree-dew/mcp-bookmark.git",
        "mcp-bookmark-server"
      ],
      "env": {
        "OPENAI_API_KEY": "your-openai-api-key-here"
      }
    }
  }
}
```

### Zed Editor

Add to your Zed settings under MCP servers:

```json
{
  "mcp": {
    "servers": {
      "bookmark": {
        "command": "/usr/local/bin/uvx",
        "args": [
          "--from",
          "git+https://github.com/pree-dew/mcp-bookmark.git",
          "mcp-bookmark-server"
        ],
        "env": {
          "OPENAI_API_KEY": "your-openai-api-key-here"
        }
      }
    }
  }
}
```

### Continue (VS Code Extension)

Add to your `continue/config.json`:

```json
{
  "mcpServers": [
    {
      "name": "bookmark",
      "command": "/usr/local/bin/uvx",
      "args": [
        "--from",
        "git+https://github.com/pree-dew/mcp-bookmark.git",
        "mcp-bookmark-server"
      ],
      "env": {
        "OPENAI_API_KEY": "your-openai-api-key-here"
      }
    }
  ]
}
```

## Available Tools

### `save_bookmark`
Save a new bookmark.

**Parameters:**
- `url` (required): The URL to bookmark
- `title` (optional): Title for the bookmark
- `description` (optional): Description

**Example:**
```json
{
  "url": "https://example.com",
  "title": "Example Site",
  "description": "A useful example website"
}
```

### `search_bookmarks`
Search through saved bookmarks.

**Parameters:**
- `query` (required): Search terms

**Example:**
```json
{
  "query": "python tutorial"
}
```

## Usage Examples

Once configured with your MCP host, you can use natural language:

- **"Save this bookmark: https://python.org with title 'Python Official'"**
- **"Search my bookmarks for React tutorials"**
- **"Find bookmarks about machine learning"**
- **"Save https://github.com/microsoft/vscode as a development tool bookmark"**

## Requirements

- Python 3.11+
- OpenAI API key
- `uvx` package manager installed
- Internet connection for GitHub repository access

## Environment Variables

- `OPENAI_API_KEY`: Required for AI-powered categorization and search enhancement

## Support

- **Issues**: [GitHub Issues](https://github.com/pree-dew/mcp-bookmark/issues)
- **MCP Documentation**: [Model Context Protocol](https://modelcontextprotocol.io/)

## License

MIT License

---

*Built for the Model Context Protocol ecosystem*
