#!/usr/bin/python3
"""lookup"""


def lookup(obj):
    """Function that retrieve the list of available attrs and methods of object

    Returns:
        object: attrs and method of the object
    """
    return dir(obj)
