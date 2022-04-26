#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        asci = ord(letter)
        if 97 <= asci <= 122:
            asci -= 32
        else:
            pass
        print("{}".format(chr(asci)), end='')
    print("")
