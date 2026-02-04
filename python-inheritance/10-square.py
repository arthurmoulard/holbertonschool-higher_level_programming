#!/usr/bin/python3
"""This module defines a Square class that inherits from a Rectangle and validates its size."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class represents a square shape with equal width and height, extending the Rectangle class."""

    def __init__(self, size):
        """Initializes a square instance after validating its size and setting both width and height to it."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size__ = size
