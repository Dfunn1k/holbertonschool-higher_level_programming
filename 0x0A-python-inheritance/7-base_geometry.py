#!/usr/bin/python3
"""In this file create a class with method that not implemented"""


class BaseGeometry:
    """class construction in process"""
    def area(self):
        """Method not is implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value.
        Args:
            * name (str): name of the object.
            * value (int): data integer.
        """
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
