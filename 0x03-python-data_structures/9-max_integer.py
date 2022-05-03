#!/usr/bin/python3
def max_integer(my_list=[]):
    """Finds the biggest integer of a list"""
    if my_list == []:
        return None

    cpy_list = my_list.copy()
    cpy_list.sort(reverse=True)

    return cpy_list[0]
