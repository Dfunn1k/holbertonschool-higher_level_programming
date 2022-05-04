#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """ Prints a dictionary by oredered keys"""
    for key1, value1 in sorted(a_dictionary.items()):
        print(f"{key1}: {value1}")
