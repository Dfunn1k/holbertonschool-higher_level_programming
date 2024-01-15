#!/usr/bin/python3
"""In this file we'll create a function that read a file and print in stdout"""


def read_file(filename=""):
    """Function that reads a text file and prints it to stdout.
    Args:
        filename (file descriptor): var where it stored a file"""
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
    print(read_data, end="")
