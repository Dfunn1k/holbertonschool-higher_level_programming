#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_copy = my_list.copy()
    length = len(list_copy)

    if (idx < 0) or (idx >= length):
        return list_copy

    list_copy[idx] = element

    return list_copy
