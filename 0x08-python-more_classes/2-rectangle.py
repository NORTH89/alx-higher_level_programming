#!/usr/bin/python3


class Rectangle:
    def __init__(self, width=0, height=0):
        """Initializes a new instance of the class."""

        self.width = width
        self.height = height

    @property
    def height(self):
        """
        Returns the value of the `height` attribute.

        :return: The value of the `height` attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter function for the 'height' attribute.

        Parameters:
            value (int): The new value for the 'height' attribute.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        Get the width of the object.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the 'width' attribute.

        Parameters:
            value (int): The new value for the 'width' attribute.

        Raises:
            TypeError: If the 'value' is not an integer.
            ValueError: If the 'value' is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        :return: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of a rectangle.

        Returns:
            The perimeter of the rectangle as an integer.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
