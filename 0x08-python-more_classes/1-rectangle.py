#!/usr/bin/python3
"""Defines a Rectangle class with width and height attributes."""


class Rectangle():
    """
    A Rectangle class with private width and height attributes.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle with optional width and height.
        Args:
          - width (default = 0): int
          - height (default = 0): int
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Gets the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width.
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
        """Gets the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height.
        Args:
          - value: int
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value
