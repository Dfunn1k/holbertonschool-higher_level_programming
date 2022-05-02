#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers"""

    for rows in matrix:
        fila = "i".join([str(x) for x in rows])
        print(fila)
