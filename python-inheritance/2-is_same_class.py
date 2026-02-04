#!/usr/bin/python3
"""This module provides a function that checks whether an object belongs exactly to a given class."""

def is_same_class(obj, a_class):
    """Checks if the given object is exactly an instance of the specified class."""
    return type(obj) is a_class
