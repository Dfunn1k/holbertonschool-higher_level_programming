#!/usr/bin/python3
def element_at(my_list, idx):
    lenght = len(my_list)
    if idx < 0:
        return None

    if idx - 1 > lenght:
        return None

    return my_list[idx - 1]


print(element_at(list(range(15)), 1))
