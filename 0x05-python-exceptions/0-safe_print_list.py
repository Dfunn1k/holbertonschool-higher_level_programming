#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """prints x elements of a list"""
    count = 0
    try:
        for i in range(0, x):
            print(f"{my_list[i]}", end='')
            count += 1
        print("")
    except IndexError:
        print("")
    return count
