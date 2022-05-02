#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """prints all integers of a list, in
    reverse order"""
    if my_list is None:
        return None
    cpylist = my_list
    cpylist.reverse()
    for num in cpylist:
        print("{:d}".format(num))
