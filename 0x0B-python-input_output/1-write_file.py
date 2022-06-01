#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file (UTF8).

    Return:
        The number of characters written
        """
    with open(filename, 'w', encoding="utf") as f:
        write_data = f.write(text)
    return len(text)
