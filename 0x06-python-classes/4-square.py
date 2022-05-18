#!/usr/bin/python3
"""Class about square"""


class Square:
    """
    Define a square by:
    private instance attribute(size)
    instation with optional size
    """

    def __init__(self, size=0):
        """
        Initialize the object
        Args:
            arg1 (int)
        """
        self.__size = size

    @property
    def size(self):
        """ retrieve size """
        return self.__size

    @size.setter
    def size(self, size):
        """for set it"""
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Return: the area of square
        """
        size = self.__size
        return size * size
