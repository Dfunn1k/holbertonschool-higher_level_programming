#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    my_list_copy = my_list.copy()
    my_list_copy.sort()
    return my_list_copy[-1]
