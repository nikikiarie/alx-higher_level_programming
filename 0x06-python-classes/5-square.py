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
        """Current square length"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int)
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Area of a square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print squares with # """
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
