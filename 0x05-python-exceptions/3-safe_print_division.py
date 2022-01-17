#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        cociente = a / b
    except ZeroDivisionError:
        cociente = None
    finally:
        print("Inside result: {}".format(cociente))
        return cociente
