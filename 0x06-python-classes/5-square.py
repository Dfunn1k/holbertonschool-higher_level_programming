#!/usr/bin/python3
"""Class Square"""


class Square():
    """
    -Private instance attribute: size
    -Instantiation with optional size: def __init__
    -Public instance method: that returns the square area
    -Public instance method: that prints the square with the character #
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size to a self.__size"""
        if not type(self.__size) is int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = self.__size

    def area(self):
        """Return the square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for i in range(self.__size):
                    print("#", end="")
                print("")
