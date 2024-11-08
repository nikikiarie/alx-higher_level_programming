#!/usr/bin/python3
"""Area and Perimeter
"""


class Rectangle:
    """Represents a rectangle
    Attributes:
        number_of_instances (int): Instance count.
        print_symbol (any): Symbol for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __del__(self):
        """Decrements instance count when deleted."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares areas of two rectangles."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with width and height."""
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Returns a string representation with the # symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""

        row = str(self.print_symbol) * self.__width
        return (row + "\n") * (self.__height - 1) + row

    def __repr__(self):
        """Returns the formal string representation."""
        return f"Rectangle({self.__width}, {self.__height})"
