#!/usr/bin/python3
def roman_to_int(roman_string):

    if (type(roman_string) is not str) or (roman_string is None):
        return 0

    number_romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    length = len(roman_string)

    for i in range(length):
        if roman_string[i] == roman_string[-1]:
            total += number_romans[roman_string[i]]
        elif number_romans[roman_string[i]] < number_romans[roman_string[i + 1]]:
            total -= number_romans[roman_string[i]]
        else:
            total += number_romans[roman_string[i]]

    return total
