#!/usr/bin/python3
"""Read_file"""


def read_file(filename=""):
    """
    Function that print the content in file
    Args:
        filename: file that will be read
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())
