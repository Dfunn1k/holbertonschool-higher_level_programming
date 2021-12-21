#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if (ord(i) < 97):
            print("{}".format(i), end="")
        else:
            code = ord(i) - 32
            print("{}".format(chr(code)), end="")
