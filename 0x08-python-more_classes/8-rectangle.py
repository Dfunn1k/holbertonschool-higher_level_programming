#!/usr/bin/python3
"""define a rectangle class"""


class Rectangle:
    """define a Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Magic method for initializating with width and height.

        Args:
            width (int): width of rectangle.
            height (int): height of rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """Representation informal of the instance.

        Returns:
            String.
        """
        strprint = ""

        if (self.width == 0) or (self.height == 0):
            return strprint

        for x in range(0, self.height):
            strprint += self.width * str(self.print_symbol)
            if x != self.height - 1:
                strprint += '\n'

        return "".join(strprint)

    def __repr__(self):
        """Representation formal of the instance"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Method for eliminated an instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method that computed what is the biggest rectangle.

        Args:
            rect_1 (Rectangle): an instance of the Class Rectangle.
            rect_2 (Rectangle): an instance of the Class Rectangle.

        Raises:
            TypeError: if rect_1 not is instance of the Rectangle.
            TypeError: if rect_1 not is instance of the Rectangle.

        Returns:
            The biggest rectangle based on the area.
            If both have the same area value, return rect_1.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2
