#!/usr/bin/python3
class Square:
    """Defines a Square class with size and position."""

    def __init__(self, size=0):
        """
        Initialize a new Square.
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    
    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: Area of the square.
        """
        return self.__size ** 2