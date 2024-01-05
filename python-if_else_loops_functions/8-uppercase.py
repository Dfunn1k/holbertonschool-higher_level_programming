#!/usr/bin/python3
def uppercase(str):
    for char in str:
        char_ascii = ord(char)
        if 96 < char_ascii < 123:
            char_ascii -= 32
        print('{}'.format(chr(char_ascii)), end='')
    print('')
