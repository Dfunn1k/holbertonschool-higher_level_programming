#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Return all sum of a unique integer"""
    new_list = set(my_list)
    sum = 0

    for num in new_list:
        sum += num

    return sum
