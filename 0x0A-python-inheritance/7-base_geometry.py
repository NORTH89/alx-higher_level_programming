#!/usr/bin/python3
""" Defines a class BaseGeometry. """


class BaseGeometry:
    """Defines a class BaseGeometry."""

    def area(self):
        raise Exception("area() is not implemented")

    """ Raises an exception. """

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
