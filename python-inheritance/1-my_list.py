#!/usr/bin/python3

class MyList(list):
    """
    MyList is a class that extends the built-in list class in Python.

    Methods
    -------
    print_sorted():
        Prints the elements of the list in a sorted order.
    """

    def print_sorted(self):
        """
        Method to print the elements of the list in a sorted order.

        The sorted() function is a built-in Python function that takes an
        iterable and returns a new sorted list of the elements in the iterable.
        """
        print(sorted(self))
