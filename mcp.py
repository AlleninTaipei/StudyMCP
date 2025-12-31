from fastmcp import FastMCP

mcp = FastMCP("我的 MCP 服務器")

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add Two Nimbers"""
    result = a + b
    print("MCP_SERVER_ACTIVE")
    return result