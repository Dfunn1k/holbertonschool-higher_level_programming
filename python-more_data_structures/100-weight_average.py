#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    weight = 0
    score = 0

    for note in my_list:
        score += note[0] * note[1]
        weight += note[1]

    return score / weight
