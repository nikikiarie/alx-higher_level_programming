#!/usr/bin/python3
"""Rectangle class for area and perimeter calculations."""


class Rectangle:
    """Defines a rectangle.
    Attributes:
        number_of_instances (int): Counts active Rectangle instances.
        print_symbol (any): Symbol for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates area."""
        return self.__height * self.__width

    def perimeter(self):
        """Calculates perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the rectangle with the larger area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a square (width == height)."""
        return cls(size, size)

    def __str__(self):
        """Returns a string with # to visualize the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for _ in range(self.__height):
            rect.append(str(self.print_symbol) * self.__width)
        return "\n".join(rect)

    def __repr__(self):
        """Returns a string representation of the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Message when a rectangle is deleted."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
