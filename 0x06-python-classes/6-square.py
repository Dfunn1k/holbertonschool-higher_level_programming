#!/usr/bin/python3
""" in this file, i will create a empty class for square"""


class Square():
    """Define a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Magic mehtod for initializating with size
        Args:

            size (int): size of square
            position (tuple): position of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Property to retrieve the size.

        Property setter to set and check:
            * Size must be an integer, otherwise raise a TypeError
            * If size is less than 0, raise a ValueError
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Property to retrieve the position.

        Property setter to set and check:
            * Position must be a tuple of 2 positive integers, otherwise raise
                a TypeError
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 \
           or not isinstance(value[0], int) or value[0] < 0 \
           or not isinstance(value[1], int) or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Public instance method for calculated the area for square.

        Args:
            size (int): size of square
        Return:
            area of square
        """
        return self.__size ** 2

    def my_print(self):
        """Public instance method that prints in the stdout the square with the
        character '#'.
            * If size is equal to 0, print an empty line.
            * position should be use by using space.
            * Don’t fill lines by spaces when position[1] > 0.

            Args:
                size (int): stored the size of instance
                value (tuple): stored the values of position
        """
        size = self.__size
        value = self.__position

        if size != 0:
            if value[1] > 0:
                for i in range(value[1]):
                    print()
            for i in range(0, size):
                print(value[0] * ' ' + size * '#', end='')
                print("")
        else:
            print("")
