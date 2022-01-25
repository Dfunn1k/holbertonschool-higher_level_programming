#!/usr/bin/python3
"""Class square"""


class Square():
    """
    that defines a square by:
    -property def size(self) to retrieve it
    -property setter def size(self, value): to set it
    -instantiation
    -public instance method
    """
    def __init__(self, size=0):
        """ Initialize data"""
        self.__size = size

    @property
    def size(self):
        """retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size to a value"""
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return the square area"""
        return self.__size ** 2
