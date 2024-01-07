#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)

    if sentence != '':
        first_char = sentence[-1]
    else:
        first_char = None

    return length, first_char
