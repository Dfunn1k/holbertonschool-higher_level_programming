#!/usr/bin/python3
"""Class square"""


class Square():
    """
    Class that defines a square by:
    -private instantion
    -public instance method
    """
    def __init__(self, size=0):
        """
        Args:
            arg1 (int): size of square
        """
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Return the current square area
        """
        return (self.__size ** 2)
