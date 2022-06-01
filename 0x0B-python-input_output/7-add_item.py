#!/usr/bin/python3
"""Load, add, save"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def append_Args(argv, list1=[]):
    """function that stores the arguments in a list except the first.

    Attributes:
        lenght (int): lenght of argv
    Args:
        argv (list): Command line arguments
        list1 (list): List
    """
    lenght = len(argv)

    for i in range(1, lenght):
        list1.append(argv[i])


try:
    jsonlist = load_from_json_file('add_item.json')
except FileNotFoundError:
    jsonlist = []

append_Args(argv, jsonlist)
save_to_json_file(jsonlist, 'add_item.json')
