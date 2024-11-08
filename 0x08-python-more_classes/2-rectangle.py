#!/usr/bin/python3
"""Defines a Rectangle class with private attributes and methods"""


class Rectangle():
    """
    Rectangle class with private width and height attributes
    and public methods
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle
        Args:
            - width (default = 0): int
            - height (default = 0): int
        """
        self.height = height
        self.width = width

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    @property
    def width(self):
        """Gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width
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
        """Gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height
        Args:
            - value: int
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
