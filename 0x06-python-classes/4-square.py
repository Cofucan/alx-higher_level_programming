#!/usr/bin/python3
"""
    This module defines Square class with a private instance
    attribute, including a default argument and validation on
    the data for the attribute.

    It also includes a class method to get the area and a getter
    function for the private attribute as well as a setter function.
"""


class Square:
    """ An class definition for a square. """
    def __init__(self, size=0):
        """Initialization of instance attributes.

        Args:
            size (int): The unit length of the square.
        """
        self._validate(size)
        self.__size = size

    @property
    def size(self):
        """ Getter function for private variable size."""
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter function for private variable size.

        Args:
            value (int): The unit length of the square.
        """
        self._validate(value)
        self.__size = value

    def area(self):
        """ Returns the current square area. """
        return self.__size**2

    def _validate(self, value):
        """ Raises error is `value` is not valid.

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
