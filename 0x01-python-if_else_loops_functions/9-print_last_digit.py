#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        l_digit = number % 10
    if number < 0:
        number *= -1
        l_digit = ((number % 10))
    print("{}".format(l_digit), end="")
    return(l_digit)
