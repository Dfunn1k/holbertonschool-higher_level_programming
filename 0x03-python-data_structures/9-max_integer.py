#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return(None)
    else:
        my_list.sort(reverse=True)
        return(my_list[0])
