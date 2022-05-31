#!/usr/bin/python3
"""In this file we will check through a function if an object is an instance of
another"""


def is_same_class(obj, a_class):
    """Check if the obj is exactly an instance of the class.
    
    Args:
        * obj (object): the object to be checked.
        * a_class (class): the class against which the object will be
        compared.
        
    Return:
        True: if there is coincidence.
        False: otherwise.
    """
    if a_class is object:
        return False
    elif isinstance(obj, a_class):
        return True
    else:
        return False
