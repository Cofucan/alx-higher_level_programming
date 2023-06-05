#!/usr/bin/python3
""" This module contains an empty class `Rectangle`. """


class Rectangle:
    """ Definition of a Rectangle class. """

    def __init__(self, width: int = 0, height: int = 0):
        self._validate_width(width)
        self._validate_height(height)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Getter function for private variable, width """
        return self.__width

    @width.setter
    def width(self, width: int):
        """ Setter function for private variable, width.

        Args:
            width (int): The new width to set.
        """
        self._validate_width(width)
        self._width = width

    @property
    def height(self):
        """ Getter function for private variable, height """
        return self.__height

    @height.setter
    def height(self, height: int):
        """Setter function for private variable, height.

        Args:
            height (int): The new height to set.
        """
        self._validate_height(height)
        self.__height = height

    def _validate_width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")

    def _validate_height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("heigth must be >= 0")
