from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Simple MCP Server")

def main():
    mcp.run()

# Add a tip calculator tool
@mcp.tool()
def calculate_tip(bill_amount: int, tip_percentage: float = 0.15) -> float:
    """Calculate tips for a given bill amount and tip percentage"""
    tip_amount = round(bill_amount * tip_percentage, 2)
    return tip_amount

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

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

if __name__ == "__main__":
    main()