#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        name = "Dany"
        pint(name)
    except NameError:
        print(message)
