#!/usr/bin/python3
class Square:
    """Defines a Square class with size and position."""
    
    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """
    Retrieve the size of the square.

    Returns:
        int: The size of the square.
    """
        return self.__size

    @size.setter
    def size(self, value):
        """
    Set the size of the square.

    Args:
        value (int): The new size of the square.
    """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the '#' character.
        """
        if self.__size == 0:
            print("")

        else:
            for index in range(self.size):
                for index2 in range(self.size):
                    print("#", end="")
                print()
                