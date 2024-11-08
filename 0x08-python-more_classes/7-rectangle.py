#!/usr/bin/python3
"""Area and Perimeter"""


class Rectangle:
    """Defines a rectangle.

    Attributes:
        number_of_instances (int): Tracks instances.
        print_symbol (any): Symbol for string display.
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
        """Sets width, ensuring it's a positive integer."""
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
        """Sets height, ensuring it's a positive integer."""
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
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Prints rectangle with `print_symbol`."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = []
        for i in range(self.__height):
            [rectangle.append(str(self.print_symbol))
             for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return "".join(rectangle)

    def __repr__(self):
        """String representation for debugging."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Handles instance deletion."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
