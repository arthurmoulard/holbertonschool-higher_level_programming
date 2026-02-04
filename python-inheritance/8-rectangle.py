#!/usr/bin/python3
"""This module defines a rectangle class that inherits validation behavior from a geometric base class."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class represents a rectangle defined by a width and a height."""

    def __init__(self, width, height):
        """Initializes a rectangle instance after validating its width and height values."""
        self.integer_validator("width", width)
        self.__width__ = width
        self.integer_validator("height", height)
        self.__height__ = height
