#!/bin/usr/python3
""" Defines a function that returns the JSON representation of an object"""


def to_json_string(my_obj):
    import json

    """Returns the JSON representation of an object"""
    return json.dumps(my_obj)
