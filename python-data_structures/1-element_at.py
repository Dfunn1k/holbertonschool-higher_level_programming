#!/usr/bin/python3
def element_at(my_list, idx):
    lenght = len(my_list)
    if idx < 0:
        return None

    if idx > lenght:
        return None

    return my_list[idx]
