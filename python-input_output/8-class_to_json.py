#!/usr/bin/python3
"""
This module contains a function that returns the dictionary
representation of a class instance's attributes.
"""


def class_to_json(obj):
    """
    Returns the dictionary representation of a class instance.

    Args:
        obj (object): The class instance to convert to JSON/dict.

    Returns:
        dict: A dictionary containing all attributes of the instance.
    """

# return a copy to avoid accidental modifications
    return obj.__dict__
