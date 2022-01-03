#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    count = 0
    for items in matrix:
        for num in items:
            if count == 2:
                print("{:d}".format(num), end='')
            else:
                print("{:d}".format(num), end=' ')
            count += 1
        count = 0
        print("")
