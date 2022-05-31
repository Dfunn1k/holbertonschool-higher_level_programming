#!/usr/bin/python3
"""In this file we'll create a subclass from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Subclass Square that inherited from Rectangle."""
    def __init__(self, size):
        """Instantiation with size."""
        Rectangle.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Public instance method for calculated area of square.

        Return:
            The area of square."""
        return self.__size ** 2
