# def main():
#     print("Hello from bilibili-notice-mcp-server!")

from pprint import pp
import os
from typing import Any

from bilibili_api import search, sync
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("bilibili-notice-mcp-server")


@mcp.tool()
def general_search(keyword: str) -> list[dict[str, Any]]:
    """
    General search
    Args:
        keyword: search keyword
    Returns:
        search results
    """
    return sync(search.search(keyword))


@mcp.tool()
def get_all_stared_up() -> list[str]:
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
            f.write("")


@mcp.tool()
def add_stared_up(up_name: list[str]) -> None:
    """
    Add a new UP creator to the list
    """
    with open("stared_up.txt", "a") as f:
        for up in up_name:
            f.write(f"{up}\n")


@mcp.tool()
def check_up_name(up_name: str) -> bool:
    """
    Check if the UP creator exists
    """
    return sync(search.general_search(up_name))


if __name__ == "__main__":
    pp("Starting bilibili-notice-mcp-server...")
    init_base_file()
    all_stared_up = get_all_stared_up()
    pp(all_stared_up)

    mcp.run(transport="stdio")
