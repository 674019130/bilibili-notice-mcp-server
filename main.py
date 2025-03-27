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
    General search
    Args:
        keyword: search keyword
    Returns:
        search results
    """
    return sync(search.general_search(keyword))


def get_stared_up() -> list[str]:
    """
    Get stared up from file
    """
    with open("stared_up.txt", "r") as f:
        return f.read().splitlines()


def init_base_file() -> None:
    """
    Initialize base files
    Create an empty stared_up.txt file if it doesn't exist
    This file is used to store the list of UP creators that the user follows
    """
    if not os.path.exists("stared_up.txt"):
        with open("stared_up.txt", "w") as f:
            pass


if __name__ == "__main__":
    print("Starting bilibili-notice-mcp-server...")
    init_base_file()

    mcp.run(transport="stdio")
