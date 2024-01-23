#!/usr/bin/python3
"""Exact same object"""


def is_same_class(obj, a_class):
    """
    Checks if an object is an instance of a specified class.

    Parameters
    ----------
    obj : object
        The object to check.
    a_class : class
        The class to check against.

    Returns
    -------
    bool
        True if the object is an instance of the specified class,
        False otherwise.
    """
    return type(obj) is a_class
