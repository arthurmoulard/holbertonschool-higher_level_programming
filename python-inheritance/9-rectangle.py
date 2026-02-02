#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width__ = width
        self.integer_validator("height", height)
        self.__height__ = height
    
    def area(self):
        return self.__width__ * self.__height__
    
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width__, self.__height__)
    