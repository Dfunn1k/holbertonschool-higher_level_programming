#!/usr/bin/python3
"""In this file we will check by means of a function if an object is an
instance of, or an instance of class that inherits"""


def is_kind_of_class(obj, a_class):
    """Check if the object is an instance of, or if the object is an instance
    of a class that inherited from, teh specified class.

    Args:
        * obj (object): the object to be checked.
        * a_class (class): the class against which the object will be
        compared.

    Return:
        True: if there is coincidence.
        False: otherwise.
    """
    return isinstance(obj, a_class)
