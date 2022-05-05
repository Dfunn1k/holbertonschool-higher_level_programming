#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0

    list_Converted = []
    roman_Letter = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    for letter in roman_string:
        if letter in roman_Letter:
            list_Converted.append(roman_Letter.get(letter))

    lenght = len(list_Converted) - 1
    sum = 0
    for i in range(0, lenght + 1):
        if i == lenght:
            sum += list_Converted[i]
        elif list_Converted[i] >= list_Converted[i + 1]:
            sum += list_Converted[i]
        else:
            sum -= list_Converted[i]
    return sum
