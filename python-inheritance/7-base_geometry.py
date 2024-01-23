#!/usr/bin/python3
"""Geometry module"""


class BaseGeometry:
    """
    BaseGeometry is a base class for geometric shapes.
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
