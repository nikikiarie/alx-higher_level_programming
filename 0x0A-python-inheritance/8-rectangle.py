#!/usr/bin/python3
"""Defines class rectangle that inherits BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rep a rectangle inheriting BaseGeo"""

    def __init(self, width, height):
        """Initialize new Rectangle"""

    self.integer_validator("width", width)
    self.__width = width
    self.integer_validator("height", height)
    self.__height = height
        
