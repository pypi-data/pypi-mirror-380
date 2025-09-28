# WATHQ MCP Server

MCP server for Saudi company lookup via WATHQ API.

## Install

```bash
pip install wathq-mcp-server
```

## Setup

1. Get API key from [developer.wathq.sa](https://developer.wathq.sa/)
2. Set environment variable:
   ```bash
   export WATHQ_API_KEY="your_api_key"
   ```

## Usage

```bash
wathq-mcp-server
```

## Claude Desktop

```json
{
  "mcpServers": {
    "wathq": {
      "command": "wathq-mcp-server",
      "env": {
        "WATHQ_API_KEY": "your_api_key"
      }
    }
  }
}
```
