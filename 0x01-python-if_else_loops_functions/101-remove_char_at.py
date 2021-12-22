#!/usr/bin/python3
def remove_char_at(str, n):
    for i in str:
        if n <= len(str) and n > 0:
            if i == str[n]:
                continue
            print("{}".format(i), end="")
        else:
            print("{}".format(i), end="")
    return("\0")
