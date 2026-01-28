#!/usr/bin/python3
"""A class Rectangle that defines a rectangle by: (based on 0-rectangle.py)"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """Parameters of the rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter: return the width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """Getter: return the height of the rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        """Setter: the witdh of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter: the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.__height * self.__width
    
    def perimeter(self):
        """ Return the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)
    
def __str__(self):
    if self.__width == 0 or self.__height == 0:
        return ""

    Space = ""
    for i in range(self.__height):
        Space += "#" * self.__width
        if i != self.__height - 1:
            Space += "\n"
    return Space
    