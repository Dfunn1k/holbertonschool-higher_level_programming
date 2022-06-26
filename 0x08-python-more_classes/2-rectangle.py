#!/usr/bin/python3
"""define a rectangle class"""


class Rectangle:
    """define a Rectangle"""
    def __init__(self, width=0, height=0):
        """Magic method for initializating with width and height.

        Args:
            width (int): width of rectangle.
            height (int): height of rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property to retrieve the width.

        Property setter to set that check:
            * Width must be an integer, otherwise raise a TypeError.
            * If witdh is less than 0, raise a ValueError.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property to retrieve the height

        Property setter to set that check:
            * Height must be an interger, otherwise raise a TypeError.
            * If height is less than 0, raise a ValueError.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method that computed the area.

        Returns:
            The rectangle area.
        """
        return (self.width * self.height)

    def perimeter(self):
        """Public instance method that computed the perimeter.

        Returns:
            the rectangle perimeter.
        """
        if (self.width == 0) or (self.height == 0):
            return 0
        return (self.width + self.height) * 2

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
