#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializes a square with a given size.
        Args:
            size (int, optional): Size of the square.
                Defaults to 0.
        """
        self.__size = size

    @property
    def size(self):
        """Getter method to retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square.
        Args:
            value (int): New size value.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

