#!/usr/bin/python3
def no_c(my_string):
    my_new_string = ""

    for character in my_string:
        if character != 'c' and character != 'C':
            my_new_string += character

    return(my_new_string)
