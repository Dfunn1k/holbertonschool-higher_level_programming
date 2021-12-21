#!/usr/bin/python3
def uppercase(str):
    for i in str:
        code = ord(i) - 32
        print("{}".format(i if ord(i) < 97 else chr(code)), end="")
    print("")
