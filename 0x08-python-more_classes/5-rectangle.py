#!/usr/bin/python3
"""
Rectangle class with width and height attributes, and relevant methods.
"""


class Rectangle():
    """
    Rectangle class with width, height attributes, and methods for area,
    perimeter, string representation, and more.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle with width and height.
        Args:
            - width (default = 0): int
            - height (default = 0): int
        """
        self.height = height
        self.width = width

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of the rectangle, or 0 if either dimension is 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Return a string representation of the rectangle using #."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(['#' * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Return the official string representation of the rectangle."""
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """Print a message when the rectangle is deleted."""
        print('Bye rectangle...')

    @property
    def width(self):
        """Return the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.
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
        """Return the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.
        Args:
            - value: int
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
