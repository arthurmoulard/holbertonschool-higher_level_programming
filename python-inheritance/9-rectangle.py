#!/usr/bin/python3
"""This module defines a Rectangle class that inherits from a base geometry class and adds area computation and string representation."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class represents a rectangle shape defined by width and height, with area calculation and custom string display."""

    def __init__(self, width, height):
        """Initializes a rectangle instance after validating its width and height values."""
        self.integer_validator("width", width)
        self.__width__ = width
        self.integer_validator("height", height)
        self.__height__ = height

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width__ * self.__height__

    def __str__(self):
        """Returns a formatted string representation of the rectangle with its dimensions."""
        return "[Rectangle] {}/{}".format(self.__width__, self.__height__)
