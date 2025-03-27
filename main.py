# def main():
#     print("Hello from bilibili-notice-mcp-server!")

import os
from typing import Any

from bilibili_api import search, sync
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("bilibili-notice-mcp-server")


@mcp.tool
def general_search(keyword: str) -> list[dict[str, Any]]:
    """
    通用搜索
    Args:
        keyword: 搜索关键词
    Returns:
        搜索结果
    """
    return sync(search.general_search(keyword))


def get_stared_up() -> list[str]:
    """
    get stared up from file
    """
    with open("stared_up.txt", "r") as f:
        return f.read().splitlines()


def init_base_file() -> None:
    """
    初始化基础文件，只有第一次执行且本地没有基础文件时执行
    """
    if not os.path.exists("stared_up.txt"):
        with open("stared_up.txt", "w") as f:
            pass


if __name__ == "__main__":
    print("Starting bilibili-notice-mcp-server...")
    init_base_file()

    mcp.run(transport="stdio")
