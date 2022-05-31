#!/usr/bin/python3
"""in this file we are going to check with a function if the object is an
instance of a class that inherited (directly or indirectly) from the specified
class"""


def inherits_from(obj, a_class):
    """Check if the object is an instance of a class that inherited directly
    or indirectly from the specified class

    Args:
        * obj (object): the object to be checked.
        * a_class (class): the class against which the object will be
        compared.

    Return:
        True: if there is coincidence.
        False: otherwise.
    """
    return issubclass(obj, a_class)
