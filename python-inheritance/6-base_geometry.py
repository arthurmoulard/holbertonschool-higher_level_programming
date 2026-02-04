#!/usr/bin/python3
"""This module defines a base class for geometric shapes with a method meant to be overridden."""

class BaseGeometry:
    """This class represents a generic geometric shape used as a parent for other shapes."""

    def area(self):
        """Raises an exception to indicate that the area method is not implemented."""
        raise Exception("area() is not implemented")
