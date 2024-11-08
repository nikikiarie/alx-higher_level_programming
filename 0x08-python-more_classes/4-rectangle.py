#!/usr/bin/python3
"""
A Rectangle class with private attributes width and height
and methods for calculation and string representation.
"""


class Rectangle():
    """
    A Rectangle class with private width, height attributes and
    various methods.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.
        Args:
            - width (default 0): int
            - height (default 0): int
        """
        self.height = height
        self.width = width

    def area(self):
        """Returns the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Returns a string representation of the Rectangle using #."""
        if self.__width == 0 or self.__height == 0:
            return ""

        final = [character * self.__width for character in '#' * self.__height]

        return '\n'.join(final)

    def __repr__(self):
        """Returns an official string representation of the Rectangle."""
        return f'Rectangle({self.__width}, {self.__height})'

    @property
    def width(self):
        """Gets the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the Rectangle.
        Args:
            - value: int
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """Gets the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the Rectangle.
        Args:
            - value: int
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value
