#!/usr/bin/python3
"""Square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """
        Constructs a new instance of the Square class.

        Parameters
        ----------
        size : int
            The size of the square's side
        """
        self.integer_validator(self, "size", size)
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns
        -------
        int
            The area of the square, calculated as the square of its side length.
        """
        return self.__size ** 2
