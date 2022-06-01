#!/usr/bin/python3
"""Load, add, save"""
from sys import argv
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def append_Args(argv):
    """function that stores the arguments in a list except the first.

    Attributes:
        listtmp (list) : here we will store the arguments.
        lenght (int) : lenght of argv
    Args:
        argv (list) : Command line arguments
    Return:
        listtmp
    """
    listtmp = []
    lenght = len(argv)

    for i in range(1, lenght):
        listtmp.append(argv[i])

    return listtmp


file_name = 'add_item.json'

if path.isfile(file_name):
    list_convert = load_from_json_file(file_name)
    list_convert += append_Args(argv)
    save_to_json_file(list_convert, file_name)
else:
    list_convert = append_Args(argv)
    save_to_json_file(list_convert, file_name)
