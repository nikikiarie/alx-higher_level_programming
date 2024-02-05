#!/usr/bin/python3
"""defines base geometry class"""


class BaseGeometry:
    """Represent base geometry"""

    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate params

        Args:
            name (str): name of params
            value: params to check
        Raises:
            TypeError: if not int
            ValueError: if not <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
