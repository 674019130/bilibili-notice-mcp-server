from typing import Any
from bilibili_api import search, sync


def general_search(keyword: str) -> list[dict[str, Any]]:
    """
    General search
    Args:
        keyword: search keyword
    Returns:
        search results
    """
    return sync(search.search(keyword))


def get_all_stared_up() -> list[str]:
    """
    Get stared up from file
    """
    with open("resource/stared_up.txt", "r") as f:
        return f.read().splitlines()


def add_stared_up(up_name: list[str]) -> None:
    """
    Add a new UP creator to the list
    """
    with open("resource/stared_up.txt", "a") as f:
        for up in up_name:
            f.write(f"{up}\n")


def check_up_name(up_name: str) -> bool:
    """
    Check if the UP creator exists
    """
    return sync(search.general_search(up_name))
