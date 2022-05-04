#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all ocurrences of an element
    by another in a new list"""

    def check(x): return x if x != search else replace
    new_list = list(map(check, my_list))
    return new_list
