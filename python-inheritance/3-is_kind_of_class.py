#!/usr/bin/python3
"""This module provides a function that checks whether an object is an instance of a given class or its subclasses."""

def is_kind_of_class(obj, a_class):
    """Determines if the object is an instance of the specified class or of a class that inherits from it."""
    return isinstance(obj, a_class)
