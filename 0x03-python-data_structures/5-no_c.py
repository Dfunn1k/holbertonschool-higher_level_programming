#!/usr/bin/python3
def no_c(my_string):
    """removes all character
    c and C from a string"""

    new_string = "".join([c for c in my_string if c != 'C' and c != 'c'])
    return new_string
