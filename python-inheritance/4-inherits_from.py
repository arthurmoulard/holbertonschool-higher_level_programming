#!/usr/bin/python3
"""This module provides a function that checks whether an object inherits from a specified class."""

def inherits_from(obj, a_class):
    """Checks if the object is an instance of a subclass of the specified class but not of the class itself."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
