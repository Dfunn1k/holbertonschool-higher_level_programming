#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if char == str[-1]:
            print('{}'.format(chr(ord(char.lower()) - 32)))
        else:
            print('{}'.format(chr(ord(char.lower()) - 32)), end='')
