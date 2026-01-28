#!/usr/bin/python3
class Square:
    """Defines a Square class with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        # Validate size type
        if type(size) is not int:
            raise TypeError("size must be an integer")
        # Validate size value
        if size < 0:
            raise ValueError("size must be >= 0")

        # Initialize private attributes
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieve the position of the square.

        Returns:
            tuple: Position of the square (x, y).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): New position (x, y).

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(i, int) for i in value) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: Area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """
        Print the square using the '#' character.

        The square is printed according to its size and position.
        """
        if self.size == 0:
            return

        else:
            # Print vertical offset
            for retour in range(self.position[1]):
                print("")

            # Print square rows
            for index in range(self.size):
                for space in range(self.position[0]):
                    print(" ", end="")
                for index2 in range(self.size):
                    print("#", end="")
                print()
                