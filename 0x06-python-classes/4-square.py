#!/usr/bin/python3
"""Defines a square"""

class Square:
    "Square"

    def __init__(self,size=0):
        """Constructor.

        Args:
            size (int): length
        """
        self.size = size
    @property
    def size(self):
            "Current square length"
            return (self.__size)
    @size.setter
    def size(self, value):
            if not isinstance(size, int):
                raise TypeError('size must be an integer')
            if size < 0:
                raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Area of a square"""
        return (self.__size * self.__size)
