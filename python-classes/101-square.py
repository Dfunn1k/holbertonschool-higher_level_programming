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
        if self.__size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for j in range(0, self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    def __str__(self):
        msg_str = ""
        if self.__size == 0:
            return msg_str
        else:
            for i in range(self.position[1]):
                msg_str += "\n"
            for j in range(0, self.size):
                msg_str += " " * self.position[0]
                msg_str += "#" * self.size
                if j != (self.size - 1):
                    msg_str += '\n'
        return msg_str
