#!/usr/bin/python3
"""Python data structure represented by a JSON string
"""
import json


def load_from_json_file(filename):
    """Function that creates a Python object from a JSON file"""

    with open(filename) as f:
        return json.load(f)
