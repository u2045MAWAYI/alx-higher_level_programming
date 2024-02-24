class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a square
        Args:
            size (float or int): size of a side of the square (default 0)
        Raises:
            TypeError: if size is not a number
            ValueError: if size is less than 0
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square
        Args:
            value (float or int): size of a side of the square
        Raises:
            TypeError: if value is not a number
            ValueError: if value is less than 0
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate the area of the square
        Returns:
            float: the area of the square
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares are equal based on area
        Args:
            other (Square): another square object
        Returns:
            bool: True if the areas are equal, False otherwise
        """
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal based on area
        Args:
            other (Square): another square object
        Returns:
            bool: True if the areas are not equal, False otherwise
        """
        return not self == other

    def __gt__(self, other):
        """Check if the area of the square is greater than another square
        Args:
            other (Square): another square object
        Returns:
            bool: True if the area is greater, False otherwise
        """
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if the area of the square is greater than or equal to another square
        Args:
            other (Square): another square object
        Returns:
            bool: True if the area is greater than or equal, False otherwise
        """
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() >= other.area()

    def __lt__(self, other):
        """Check if the area of the square is less than another square
        Args:
            other (Square): another square object
        Returns:
            bool: True if the area is less, False otherwise
        """
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() < other.area()

    def __le__(self, other):
        """Check if the area of the square is less than or equal to another square
        Args:
            other (Square): another square object
        Returns:
            bool: True if the area is less than or equal, False otherwise
        """
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() <= other.area()
