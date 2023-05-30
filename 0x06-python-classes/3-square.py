#!/usr/bin/python3
"""
    This module defines Square class with a private instance
    attribute, including a default argument.
"""


class Square:
    """ An class definition for a square. """
    def __init__(self, size=0):
        """Initialization of instance attributes.

        Args:
            size (int): The unit length of the square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """ Returns the current square area. """
        return self.__size**2
