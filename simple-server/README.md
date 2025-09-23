# Creating a baseline MCP Server using the MCP Python SDK

Follow this tutorial to create a simple MCP server with an example resource, tool, and prompt.

For more baseline examples see the [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Requirements

- uv<br />
    
    [Official UV documentation](https://docs.astral.sh/uv/getting-started/installation/)
    
    #### MacOS / Linux:
    Use curl to download the script and execute it with sh:

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

    #### Windows:
    Use irm to download the script and execute it with iex:

    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | ie
    ```
  </details><br />
- [Visual Studio Code](https://code.visualstudio.com/)
- For testing in Claude:
  - [Claude.ai account](https://claude.ai) (MCP support is available for all account types)
  - [Claude Desktop app](https://claude.ai/download), available for macOS and Windows

## Build an MCP Server from Scratch

### Step 1: Create a UV-managed project

Initate a new project and go to the folder:

```bash
uv init simple-mcp-server
cd simple-mcp-server
```

Start the UV project:

```bash
uv sync
```

Start the virtual environment:

In terminal:
```bash
source .venv/bin/activate
```

For later: To stop the virtual environment:

```bash
deactivate
```

Add the MCP Python SDK:

```bash
uv add "mcp[cli]"
```

Set the VS Code python environment:

1. Open the Command Palette Shift + CMD/CTRL + P
2. Select "Python: Set Project Environment
3. Choose `simple-mcp-server` venv

###  Step 2: Set up the main file

Rename `main.py` to `server.py` and replace the content with the following:

```python
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Simple MCP Server")

def main():
    mcp.run()

if __name__ == "__main__":
    main()
```

### Step 3: Register the server

In `pyproject.toml`:

```json
[project.scripts]
simple-mcp-server = "server:main"
```

Add a blank `__init__.py` file.

### Step 4: Add Tools, Resources, and Prompts

#### Tools

Tools are used by the LLM to perform actions that have side-effects. 

Official spec: https://modelcontextprotocol.io/docs/concepts/tools 
SDK docs: https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file#tools

Add a Tool:

```python
# Add a tip calculator tool
@mcp.tool()
def calculate_tip(bill_amount: int, tip_percentage: float = 0.15) -> float:
    """Calculate tips for a given bill amount and tip percentage"""
    return bill_amount * tip_percentage
```

#### Resources

Official spec: https://modelcontextprotocol.io/docs/concepts/resources 
SDK docs: https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file#resources

Add a Resource:

```python
# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

#### Prompts

Official spec: https://modelcontextprotocol.io/docs/concepts/prompts 
SDK docs: https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file#prompts

Add a Prompt:

```python
# Add a prompt for generating greetings in different styles
@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    """Generate a greeting prompt"""
    styles = {
        "friendly": "Please write a warm, friendly greeting in Danish",
        "formal": "Please write a formal, professional greeting in Danish",
        "casual": "Please write a casual, relaxed greeting in Danish",
    }

    return f"{styles.get(style, styles['friendly'])} for someone named {name} in Danish."
```

### 5. Run MCP server in dev mode with the [MCP Inspector](https://github.com/modelcontextprotocol/inspector)

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