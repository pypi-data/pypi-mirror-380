from fastmcp import FastMCP

mcp = FastMCP(name="test_mcp_server")


@mcp.tool()
def add(a: float, b: float) -> float:
    """加法运算
    参数:
    a: 第一个数字
    b: 第二个数字
    返回:
    两数之和
    """
    return a + b


@mcp.tool()
def subtract(a: float, b: float) -> float:
    """减法运算
    参数:
    a: 第一个数字
    b: 第二个数字
    返回:
    两数之差 (a - b)
    """
    return a - b


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """乘法运算
    参数:
    a: 第一个数字
    b: 第二个数字
    返回:
    两数之积
    """
    return a * b


@mcp.tool()
def divide(a: float, b: float) -> float:
    """除法运算
    参数:
    a: 被除数
    b: 除数
    返回:
    两数之商 (a / b)
    异常:
    ValueError: 当除数为零时
    """
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

# def run():
#     mcp.run(transport='streamable-http', host="0.0.0.0", port=8001)
#
# if __name__ == "__main__":
#     run()
