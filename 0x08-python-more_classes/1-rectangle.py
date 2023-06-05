#!/usr/bin/python3
""" This module contains an empty class `Rectangle`. """


class Rectangle:
    """ Definition of a Rectangle class. """

    def __init__(self, width=0, height=0):
        self.__validate_width(width)
        self.__validate_height(height)
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter function for private variable, width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter function for private variable, width.

        Args:
            value (int): The new width to set.
        """
        self.__validate_width(value)
        self.__width = value

    @property
    def height(self):
        """ Getter function for private variable, height """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function for private variable, height.

        Args:
            value (int): The new height to set.
        """
        self.__validate_height(value)
        self.__height = value

    def __validate_width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")

    def __validate_height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("heigth must be >= 0")
