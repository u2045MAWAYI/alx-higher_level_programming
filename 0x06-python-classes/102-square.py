#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square
    Attributes:
        __side_length (int): size of a side of the square
    """
    def __init__(self, side_length=0):
        """initializes the square
        Args:
            side_length (int): size of a side of the square
        Returns:
            None
        """
        self.side_length = side_length

    def area(self):
        """calculates the square's area
        Returns:
            The area of the square
        """
        return (self.__side_length) ** 2

    @property
    def side_length(self):
        """getter of __side_length
        Returns:
            The size of the square
        """
        return self.__side_length

    @side_length.setter
    def side_length(self, value):
        """setter of __side_length
        Args:
            value (int): the size of a size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("side_length must be an integer")
        else:
            if value < 0:
                raise ValueError("side_length must be >= 0")
            else:
                self.__side_length = value

    def __lt__(self, other):
        """Compare if square is less than another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.side_length < other.side_length

    def __le__(self, other):
        """Compare if square is less than or equal to another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.side_length <= other.side_length

    def __eq__(self, other):
        """Compare if square is equal to another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.side_length == other.side_length

    def __ne__(self, other):
        """Compare if square is not equal to another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.side_length != other.side_length

    def __ge__(self, other):
        """Compare if square is greater than or equal to another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.side_length >= other.side_length

    def __gt__(self, other):
        """Compare if square is greater than another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.side_length > other.side_length
