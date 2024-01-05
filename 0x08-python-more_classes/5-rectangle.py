#!/usr/bin/python3
""" Defines a Rectangle class. """


class Rectangle:
    """Defines a Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle."""
        self.width = width
        self.height = height

    @property
    def height(self):
        """Returns the value of the `height` attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the object."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Returns the value of the `width` attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the object."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Return area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + 2 * self.__height)

    def __str__(self):
        """Return printable representation of the Rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr__(self):
        """Return string representation of the Rectangle."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Delete an instance of Rectangle."""
        print("Bye rectangle...")
