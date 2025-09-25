# Hands-On MCP: Connect Anything to AI | A Future Product Days 2025 workshop by @mor10

Supporting documents for the ["Hands-On MCP: Connect Anything to AI" workshop at Future Product Days 2025](https://www.futureproductdays.com/session/www-futureproductdays-com-session-mini-workshop-afternoon-understanding-is-all-you-need-beyond-the-basics-with-ai-apis).

## What you'll need to follow this workshop 

- A laptop with an internet connection
- A [GitHub](https:/github.com) account (free, pro, edu, or enterprise)
- [VS Code](https://code.visualstudio.com/) with GitHub Copilot installed
- A [Claude](https://claude.ai) account (free works, pro is better for experimentation)
- A [Zapier](https://mcp.zapier.com) account (free is sufficient)
- A healthy disrespect for the sanctity of technology (and your computer)

## 🧑‍💻 Hands-On Exercise #1: Give Claude Desktop (Almost) Unlimited Powers with Zapier MCP Server

### Step 0: Join the Undestroyers Slack for experimentation

Visit this invite link and go through the process to join: [https://join.slack.com/t/undestroyers/shared_invite/zt-3eiyedlb4-8mh4Pg84dFOvQHkmrWv6Rw](https://join.slack.com/t/undestroyers/shared_invite/zt-3eiyedlb4-8mh4Pg84dFOvQHkmrWv6Rw)

### Step 1: Set up a new MCP Server in Zapier

1. Go to [mcp.zapier.com](https://mcp.zapier.com)
2. Press the "+ New MCP Server" button
3. Under "MCP Client" use the drop-down to select "Claude"
4. Give your MCP server a recognizable name like "My Custom Zapier MCP Server"

### Step 2: Add Slack tools

1. In the new MCP Server, press the "+ Add tool" button to add tools.
2. Search for Slack
3. Under Slack, select "Find Public Channel"
4. Go through the authentication loop (Note: you must have Slack open and be logged in for this)
5. Repeat 1-3 and add "Send Channel Message"

> [!NOTE]
> Most (if not all) tools require some form of authentication, so connect to services you already have an account for.

### Step 3: Add the MCP server to Claude

1. In Zapier MCP, switch to the "Connect" tab at the top
2. Follow the step-by-step instructions on the page
3. Go through the OAuth flow when prompted
4. In Claude, click the "Search and tools" button in the chat window (looks like two faders)
5. Make sure "Zapier" shows up as an active tool (not greyed out)

If Zapier is not active:

6. In Claude, go to Settings -> Connectors 
7. Try connecting Zapier again

> [!NOTE]
> If you're using a brand new Zapier account, you may have to wait for Claude to be able to connect. This appears to be an anti-abuse feature.

### Step 4: Test the MCP server

If Zapier is active in Claude:

1. Start a new chat
2. Submit a prompt similar to this: 
```
Send a message in the #future-product-days channel saying "Success! (this message is from [insert your name])" or similar.
```
3. Wait and see what happens!

## 🧑‍💻 Hands-On Exercise #3: Build your own MCP Server

1. Clone this repo to your computer
2. Open VS Code to this project
3. Go to the `/simple-server/` folder
4. Open `README.md`
5. Follow the instructions

## 🔗 Links for Further MCP Exploration

- [Model Context Protocol: Official docs](https://modelcontextprotocol.io/)
- [GitHub MCP Registry](https://github.com/mcp)
- [MCP Registry](https://github.com/modelcontextprotocol/registry)
- [MCP GitHub Org with lots of repos](https://github.com/modelcontextprotocol)
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [LinkedIn Learning courses on MCP](https://www.linkedin.com/learning/search?entityType=COURSE&keywords=mcp)
- [Morten's infamous "Machine Controlled Pandemonium" talk](https://www.youtube.com/watch?v=5SOpKjf839)
