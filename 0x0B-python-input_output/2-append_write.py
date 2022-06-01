#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of a text file.

    Return:
        The number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        write_data = f.write(text)

    return len(text)
