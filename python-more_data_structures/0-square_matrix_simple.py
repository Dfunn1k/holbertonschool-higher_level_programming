#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    for arr in matrix:
        arr_converted = list(map(lambda x: x**2, arr))
        new_matrix.append(arr_converted)

    return new_matrix
