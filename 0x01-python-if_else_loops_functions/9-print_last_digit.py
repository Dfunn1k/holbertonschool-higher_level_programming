#!/usr/bin/python3
def print_last_digit(number):
    ld = 0
    if number < 0:
        ld = ((number * -1) % 10)
        print("{:d}".format(ld), end='')
        return ld
    else:
        ld = number % 10
        print("{:d}".format(ld), end='')
        return ld
