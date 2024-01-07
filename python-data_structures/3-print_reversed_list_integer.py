#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_in_reverse = sorted(my_list, reverse=True)

    for num in list_in_reverse:
        print('{:d}'.format(num))
