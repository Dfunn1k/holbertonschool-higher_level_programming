#!/usr/bin/python3
"""Class about square"""


class Square:
    """
    Define a square by:
    private instance attribute(size)
    instation with optional size
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the object
        Args:
            arg1 (int)
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ retrieve size """
        return self.__size

    @size.setter
    def size(self, size):
        """for set size"""
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """retrieve position"""
        return self.__position

    @position.setter
    def position(self, position):
        """ for set position"""
        if (not type(position) is tuple) and (len(position != 2)):
            raise TypeError("size must be an integer")
        self.__position = position

    def area(self):
        """
        Return: the area of square
        """
        size = self.__size
        return size * size

    def my_print(self):
        """
        Prints the square with the character #
        -if size is equal to 0, print an empty line
        -position should be use by using space
        """
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for i in range(self.__position[1]):
                    print()
            for i in range(self.size):
                print(self.__position[0]*' ' + self.__size*"#", end="")
                print()
