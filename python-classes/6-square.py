#!/usr/bin/python3
""" Its is a module for learn about class in python"""


class Square:
    """A class that build square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 \
           or not isinstance(value[0], int) or value[0] < 0 \
           or not isinstance(value[1], int) or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        return self.size ** 2

    def my_print(self):
        size = self.size
        fill = self.position

        if size != 0:
            if fill[1] > 0:
                for i in range(fill[1]):
                    print()

            for i in range(0, size):
                print(fill[0] * ' ' + size * '#', end='')
                print("")
        else:
            print("")
