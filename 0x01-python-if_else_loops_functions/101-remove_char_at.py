#!/usr/bin/python3
def remove_char_at(str, n):
    cpstr = ""
    for i in range(0, len(str)):
        if i == n:
            continue
        cpstr += str[i]
    return cpstr
