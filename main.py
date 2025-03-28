# def main():
#     print("Hello from bilibili-notice-mcp-server!")

from pprint import pp
import os
from typing import Any

from bilibili_api import search, sync
from mcp.server.fastmcp import FastMCP

from tools.general import general_search as _general_search
from tools.general import get_all_stared_up as _get_all_stared_up
from tools.general import add_stared_up as _add_stared_up
from tools.general import check_up_name as _check_up_name
from tools.up_live.status import check_up_live_status as _check_up_live_status
from init import init_base_file

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
    return _general_search(keyword)


@mcp.tool()
def get_all_stared_up() -> list[str]:
    """
    Get stared up from file
    """
    return _get_all_stared_up()


@mcp.tool()
def add_stared_up(up_name: list[str]) -> None:
    """
    Add a new UP creator to the list
    """
    _add_stared_up(up_name)


@mcp.tool()
def check_up_name(up_name: str) -> bool:
    """
    Check if the UP creator exists
    """
    return _check_up_name(up_name)


@mcp.tool()
def check_up_live_status(up_name: str) -> bool:
    """
    Check if the UP creator is live
    """
    return _check_up_live_status(up_name)


if __name__ == "__main__":
    pp("Starting bilibili-notice-mcp-server...")
    init_base_file()
    all_stared_up = get_all_stared_up()
    pp(all_stared_up)

    mcp.run(transport="stdio")
