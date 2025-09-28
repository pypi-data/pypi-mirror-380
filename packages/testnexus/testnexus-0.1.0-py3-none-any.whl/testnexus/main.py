# -*- coding: utf-8 -*-
"""
FastMCP 快速入门示例。
首先，请切换到 `examples/snippets/clients` 目录，然后运行以下命令来启动服务器：
    uv run server fastmcp_quickstart stdio
"""
# 从 mcp.server.fastmcp 模块中导入 FastMCP 类，这是构建 MCP 服务器的核心。
from mcp.server.fastmcp import FastMCP
# 创建一个 MCP 服务器实例，并将其命名为 "Demo"。
# 这个名字会向连接到此服务器的 AI 客户端展示。
mcp = FastMCP("Demo")
@mcp.tool()
def create_txt_file():
    """
      这个工具的功能是在指定目录下写入指定内容
      """
    # 文件路径
    file_path = "D:/sjnexus.txt"

    try:
        # 创建并写入文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("这是一个测试文件，csj20250927")
        print(f"文件创建成功：{file_path}")
        return True

    except Exception as e:
        print(f"文件创建失败：{e}")
        return False

@mcp.tool()
def add(a: int, b: int) -> int:
    """
    这个工具的功能是计算两个整数的和。
    文档字符串（docstring）会作为工具的描述，帮助 AI 理解其功能。
    """
    return a + b

if __name__ == "__main__":

    mcp.run(transport="stdio")