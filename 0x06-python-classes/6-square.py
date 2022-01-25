#!/usr/bin/python3
"""Class square"""


class Square():
    """
    class Square that defines a square by:
    -Private instance attribute: size
    -Private instance attribute: position
    -Instantiation with optional size and optional position
    -Public instance method: def area(self)
    -Public instance method: def my_print(self)
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialized data with:
        arg1 (int): size
        arg2 (tuple): position
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieve it size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size to a self.__size"""
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ Retrieve it position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position to a self.__position"""
        if (not type(value) is tuple) and ():
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) > 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in range(0, 2):
            if not type(value[i]) is int:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
            if value[i] < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the square area"""
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character #
        -if size is equal to 0, print an empty line
        -position should be use by using space
        """
        if self.__size == 0:
            print()
        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print()
        for i in range(self.size):
            print(self.__position[0]*'_' + self.__size*"#", end="")
            print()
