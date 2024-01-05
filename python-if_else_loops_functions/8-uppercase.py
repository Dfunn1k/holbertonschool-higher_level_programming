#!/usr/bin/python3
def uppercase(str):
    for char in str:
        print('{}'.format(chr(ord(char.lower()) - 32)), end='')
    print('')
