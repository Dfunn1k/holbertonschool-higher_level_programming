#!/usr/bin/python3
"""In this file we'll create a subclass from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Subclass from BaseGeometry.

    Args:
        * width (int): width of rectangle.
        * height (int): height of rectangle.
    """
    def __init__(self, width, height):
        """Instantiation with width and height"""
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height
