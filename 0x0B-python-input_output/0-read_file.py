#!/usr/bin/python3

def read_file(filename=""):
    """Function that reads a text file and prints it to stdout.

    Args:
        read_data (file descriptor): var where it stored a file"""
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)
