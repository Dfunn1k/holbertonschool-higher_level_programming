#!/usr/bin/python3
"""Geometry module"""


class BaseGeometry:
    """
    BaseGeometry is a base class for geometric shapes.
    """
    def area(self):
        raise Exception("area() is not implemented")
