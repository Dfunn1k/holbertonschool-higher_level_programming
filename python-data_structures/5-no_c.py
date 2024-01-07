#!/usr/bin/python3
def no_c(my_string):
    string_without_c = ''

    for char in my_string:
        if (char != 'c') and (char != 'C'):
            string_without_c += char

    return string_without_c
