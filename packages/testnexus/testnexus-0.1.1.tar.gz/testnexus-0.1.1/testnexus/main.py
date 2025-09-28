# -*- coding: utf-8 -*-
"""
FastMCP 快速入门示例。

将应用程序的启动逻辑封装在一个函数中，以作为 pyproject.toml 的脚本入口点。
"""
from mcp.server.fastmcp import FastMCP

# 1. 创建 MCP 服务器实例 (保持不变)
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

# 2. **新增：定义一个可调用的入口点函数**
def cli():
    """
    MCP 服务器的命令行入口点。
    这个函数会被打包工具调用，并负责启动 FastMCP 实例。
    """
    # 使用 stdio 传输方式运行 MCP 服务器
    mcp.run(transport="stdio")

# 保留 __main__ 块用于本地直接运行测试
if __name__ == "__main__":
    cli() # 在本地运行时调用 cli 函数
