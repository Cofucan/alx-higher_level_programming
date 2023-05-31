#!/usr/bin/python3
"""
    This module defines Square class with a private instance
    attribute, including a default argument and validation on
    the data for the attribute.

    It also includes a class method to get the area and a getter
    function for the private attribute as well as a setter function.

    Another class method for printing the square with the character #.
"""


class Square:
    """An class definition for a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialization of instance attributes.

        Args:
            size (int): The unit length of the square.
            size (int): Coordinates for printing the square.
        """
        self._validate_size(size)
        self._validate_position(position)
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter function for private variable size."""
        return self.__size

    @property
    def position(self):
        """Getter function for private variable position."""
        return self.__position

    @size.setter
    def size(self, value):
        """Setter function for private variable size.

        Args:
            value (int): The unit length of the square.
        """
        self._validate_size(value)
        self.__size = value

    @position.setter
    def position(self, data):
        """Setter function for private variable position.

        Args:
            data (tuple): Coordinates for printing the square.
        """
        self._validate_position(data)
        self.__position = data

    def area(self):
        """Returns the current square area."""
        return self.__size**2

    def my_print(self):
        """Prints the # character using the square size and coordinates."""
        if self.__size > 0:
            for _ in range(self.__position[1]):
                print("")

            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
        else:
            print("")

    def _validate_size(self, value):
        """Raises error is `value` is not valid.

        Args:
            value (int): Data to be validated.

        Raises:
            TypeError: If arg `value` is not an integer.
            ValueError: If arg `value` is negative.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def _validate_position(self, data):
        """Raises error is `data` is not valid.

        Args:
            data (tuple): Data to be validated.

        Raises:
            TypeError: If data is not a tuple with 2 positive integers.
        """
        if \
                type(data) is not tuple or \
                any(type(x) is not int for x in data) or \
                len(data) != 2 or \
                any(x < 0 for x in data):
            raise TypeError("position must be a tuple of 2 positive integers")

    def __str__(self):
        if self.__size != 0:
            for _ in range(self.__position[1]):
                print("")

        for x in range(self.__size):
            for _ in range(self.__position[0]):
                print(" ", end="")
            for _ in range(self.__size):
                print("#", end="")
            if x != self.__size - 1:
                print("")
        return ""
