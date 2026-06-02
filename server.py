from mcp.server.fastmcp import FastMCP
from datetime import datetime
mcp=FastMCP("Server")
@mcp.tool()
def hello(name: str)-> str:
    return f"Hello {name}"
@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b
@mcp.tool()
def current_time() -> str:
    return str(datetime.now())
if __name__=="__main__":
    mcp.run()