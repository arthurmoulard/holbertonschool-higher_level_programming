#!/usr/bin/python3
"""This module provides a utility function to list available attributes and methods of an object."""

def lookup(obj):
    """Returns a list of available attributes and methods of the given object."""
    return dir(obj)
