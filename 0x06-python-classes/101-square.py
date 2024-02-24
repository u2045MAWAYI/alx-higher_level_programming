#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, side_length=0, position=(0, 0)):
        """Initialize a new square.
        Args:
            side_length (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.side_length = side_length
        self.position = position

    @property
    def side_length(self):
        """Get/set the current side length of the square."""
        return self.__side_length

    @side_length.setter
    def side_length(self, value):
        if not isinstance(value, int):
            raise TypeError("side_length must be an integer")
        elif value < 0:
            raise ValueError("side_length must be >= 0")
        self.__side_length = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__side_length * self.__side_length

    def my_print(self):
        """Print the square with the # character."""
        if self.__side_length == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__side_length):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__side_length)]
            print("")

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__side_length != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__side_length):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__side_length)]
            if i != self.__side_length - 1:
                print("")
        return ("")
