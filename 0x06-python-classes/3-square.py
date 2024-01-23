#!/usr/bin/python3
"""Defines a square"""

class Square:
    "Square"

    def __init__(self,size=0):
        """Constructor.

        Args:
            size (int): length

        Raises:
            TypeError: if size not int
            ValueError: is size < 
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Area of a square"""
        return (self._size * self._size)
