#!/usr/bin/python3
"""In this file """


class MyList(list):
    """Subclass that inherits from list"""
    def print_sorted(self):
        """Method that prints the list, but sorted.

        Attributes:
            * cpy_list (list): list that copy the real list
        """
        cpy_list = self[:]
        cpy_list.sort()
        print(cpy_list)
