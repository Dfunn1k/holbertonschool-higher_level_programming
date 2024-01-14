#!/usr/bin/python3
"""This file shows a list of the methods of an object"""


def lookup(obj):
    """Function that retrieve the list of available attrs and methods of object

    Returns:
        object: attrs and method of the object
    """
    return dir(obj)
