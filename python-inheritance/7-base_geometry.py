#!/usr/bin/python3
"""This module defines a base class for geometric shapes with validation utilities."""

class BaseGeometry:
    """This class represents a generic geometric shape intended to be extended by other classes."""

    def area(self):
        """Raises an exception to indicate that the area method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that the given value is a positive integer associated with a named parameter."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
