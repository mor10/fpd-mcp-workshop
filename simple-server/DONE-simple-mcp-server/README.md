# Example MCP server


## Test MCP server in dev mode with the [MCP Inspector](https://github.com/modelcontextprotocol/inspector)

Online version:

```bash
npx @modelcontextprotocol/inspector uv run server.py
```

Local version:

```bash
uv run mcp dev server.py
```

## Run MCP server in VS Code

1. Open the Command Palette Shift + CMD/CTRL + P

2. Select "MCP: Open User Configuration". This opens `mcp.json`

3. In `mcp.json`:

  ```json
  {
    "servers": {
      "simple-server": {
        "type": "stdio",
        "command": "uv",
        "args": [
          "run",
          "--directory",
          "/absolute/path/to/simple-mcp-server",
          "server.py"
        ]
      }
    },
    "inputs": []
  }
  ```

## Run MCP server in Claude Desktop

### Automatic install

In terminal:
```bash
uv run mcp install server.py
```

### Manual install

1. Open `claude_desktop_config.js` in an editor:
 
  File location:
  - MacOS / Linux `~/Library/Application/Support/Claude/claude_desktop_config.json`
  - Windows `AppData\Claude\claude_desktop_config.json`

2. Find the full path to `uv`:
  
  - MacOS / Linux:
  ```bash
  which uv
  ```
  - Windows:
  ```bash
  where uv
  ```

2. In `claude_desktop_config.js`

  ```json
  {
    "mcpServers": {
      "Simple MCP Server": {
        "command": "/opt/homebrew/bin/uv",
        "args": [
          "run",
          "--with",
          "mcp[cli]",
          "mcp",
          "run",
          "/absolute/path/to/simple-mcp-server/server.py"
        ]
      }
    }
  }
  ```