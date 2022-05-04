#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """computes the square value
    of all integers of a matrix"""

    def pow_2(x): return x**2

    matrix2 = []

    for rows in matrix:
        squares = list(map(pow_2, rows))
        matrix2.append(squares)

    return matrix2
