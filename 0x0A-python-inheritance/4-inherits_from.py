#!/usr/bin/python3
""" function that returns True if the object is an instance of 
	a class that inherited
 """


def inherits_from(obj, a_class):
    """Checks if an object is an instance or inherited
    instance of a class
    Args:
                    obj (any): The object to check
                    a_class (type): The class to match the type of obj to
    Returns:
                    If obj is an instance or inherited instance of a_class - True
                    Otherwise - False
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
