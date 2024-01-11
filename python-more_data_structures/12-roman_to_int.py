#!/usr/bin/python3
def roman_to_int(roman_string):

    if (type(roman_string) is not str) or (roman_string is None):
        return 0

    number_roman = {
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
        if i == length - 1:
            total += number_roman[roman_string[i]]
        elif number_roman[roman_string[i]] < number_roman[roman_string[i + 1]]:
            total -= number_roman[roman_string[i]]
        else:
            total += number_roman[roman_string[i]]

    return total
