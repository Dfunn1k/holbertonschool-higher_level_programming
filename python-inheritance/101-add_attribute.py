#!/usr/bin/python3
"""Module special"""


def add_attribute(obj, attr, value):
    """
    This function adds a new attribute to an object if it's possible.

    Parameters:
    obj (object): The object to which the attribute should be added.
    attr (str): The name of the attribute to be added.
    value (any): The value of the attribute to be added.

    Raises:
    TypeError: If the object can't have new attributes added.
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
