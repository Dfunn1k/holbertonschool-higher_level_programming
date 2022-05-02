#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """prints all integers of a list, in
    reverse order"""
    my_list.reverse()
    for num in my_list:
        print("{:d}".format(num))
