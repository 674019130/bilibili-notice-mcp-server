import os


def init_base_file() -> None:
    """
    Initialize base files
    Create an empty stared_up.txt file if it doesn't exist
    This file is used to store the list of UP creators that the user follows
    """
    if not os.path.exists("resource/stared_up.txt"):
        with open("resource/stared_up.txt", "w") as f:
            f.write("")
