# AI Memory MCP Server

Model Context Protocol server that allows Claude Desktop to read from AI Memory System.

## Installation

1. Configure Claude Desktop (`~/.config/Claude/claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "ai-memory": {
      "command": "ssh",
      "args": [
        "root@YOUR_SERVER_IP",
        "python3",
        "/tmp/ai-memory-mcp/ai_memory_mcp_server.py"
      ]
    }
  }
}
```

2. Restart Claude Desktop

3. Use the tool: "Read my Council memory"

## Features

- Read Council member memories
- Access project context
- View session transcripts
- Universal AI memory access

© 2025 Blue Moon Ecosystem
