#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    for i in str:
        if (n > 0 and n <= len(str)):
            if i != str[n]:
                new_str += i
        else:
            return(str)
    return(new_str)
