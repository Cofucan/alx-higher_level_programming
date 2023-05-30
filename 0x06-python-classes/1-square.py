#!/usr/bin/python3
"""
    This module defines Square class with a private
    attribute.
"""


class Square:
    """ An class definition for a square. """
    def __init__(self, size):
        """Initialization of instance attributes.

        Args:
            size (int): The unit length of the square.
        """
        self.__size = size
