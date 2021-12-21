#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if (65 <= ord(i) <= 90):
            print("{}".format(i), end="")
        else:
            code = ord(i) - 32
            print("{}".format(chr(code)), end="")
