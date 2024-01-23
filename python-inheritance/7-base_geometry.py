#!/usr/bin/python3
"""Geometry module"""


class BaseGeometry:
    def area(self):
        """
        Calculates the area of the geometric shape.

        This method should be implemented by subclasses of BaseGeometry.

        Raises
        ------
        Exception
            If the method is not implemented by a subclass.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.

        Parameters
        ----------
        name : str
            The name of the value, used in error messages.
        value : int
            The value to validate.

        Raises
        ------
        TypeError
            If the value is not an integer.
        ValueError
            If the value is not greater than 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
