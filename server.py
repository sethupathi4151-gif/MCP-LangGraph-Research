from fastmcp import FastMCP

mcp = FastMCP("Calculator Server")


@mcp.tool
def add(a: int, b: int) -> int:
    """Adds two numbers"""
    return a + b


if __name__ == "__main__":
    print(add(10, 20))
    mcp.run()