#!/usr/bin/python3
"""Module that print attributes and methods of an object"""


def lookup(obj):
    """Function that print attributes and method of an object"""
    return [x for x in obj.__dict__]
