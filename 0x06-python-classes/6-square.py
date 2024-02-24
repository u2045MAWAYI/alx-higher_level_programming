#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square
        Args:
            size (int): size of a side of the square (default 0)
            position (tuple): position of the square (default (0, 0))
        Raises:
            TypeError: if size is not an integer or if position is not a tuple
            ValueError: if size is less than 0 or if position contains non-positive integers
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square
        Args:
            value (int): size of a side of the square
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square
        Args:
            value (tuple): position of the square
        Raises:
            TypeError: if value is not a tuple or if tuple elements are not integers
            ValueError: if tuple elements are less than 0
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(val, int) for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(val >= 0 for val in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates the area of the square
        Returns:
            int: area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character '#'"""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

