#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers"""

    for rows in matrix:
        print(" ".join("{:d}".format(x) for x in rows))
