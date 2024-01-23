#!/usr/bin/python3
"""Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a specified class or its subclasses.

    Parameters
    ----------
    obj : object
        The object to check.
    a_class : class
        The class to check against.

    Returns
    -------
    bool
        True if the object is an instance of the specified class or its
        subclasses, False otherwise.
    """
    return isinstance(obj, a_class)
