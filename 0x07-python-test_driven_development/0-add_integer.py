#!/usr/bin/python3


def add_integer(a, b=98):
    """a function that adds two integers
    Args:
            a: first integer
            b: second integer
    Returns:
            The addition of a and b
    Raises:
            TypeError: if a or b is not an integer
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
