#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializes a square
        Args:
            size (int): size of a side of the square (default 0)
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of the square
        Returns:
            int: area of the square
        """
        return self.__size ** 2
