#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for items in matrix:
        for num in items:
            print("{:d}".format(num), end=' ')
        print()
