#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements
    integers of a list"""
    count = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end='')
            count += 1
        except (ValueError, TypeError):
            pass
    print("")
    return count
