#!/usr/bin/python3
"""Geometry module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle is a subclass of BaseGeometry representing a rectangle.

    Attributes
    ----------
    __width : int
        The width of the rectangle.
    __height : int
        The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Constructs a new instance of Rectangle.

        Parameters
        ----------
        width : int
            The width of the rectangle.
        height : int
            The height of the rectangle.

        Raises
        ------
        TypeError
            If the width or height is not an integer.
        ValueError
            If the width or height is not greater than 0.
        """
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height
