#!/usr/bin/python3
def max_integer(my_list=[]):
    max_int = 0

    if not my_list:
        return None

    for num in my_list:
        if num > max_int:
            max_int = num

    return max_int
