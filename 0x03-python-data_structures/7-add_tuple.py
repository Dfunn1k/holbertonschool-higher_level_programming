#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """adds 2 tuples"""

    if len(tuple_a) < 2:
        tuple_a += (0, 0)

    if len(tuple_b) < 2:
        tuple_b += (0, 0)

    tupla_result = ((tuple_a[0] + tuple_b[0]), tuple_a[1] + tuple_b[1])

    return (tupla_result)
