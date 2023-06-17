#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self._validate_attr(width, "width")
        self._validate_attr(height, "height")
        self._validate_attr(x, "x")
        self._validate_attr(y, "y")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # >>>>>>>>>>>>>>>>>>>   WIDTH   <<<<<<<<<<<<<<<<<<<<
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self._validate_attr(value, "width")
        self.__width = value

    # >>>>>>>>>>>>>>>>>>>   HEIGHT   <<<<<<<<<<<<<<<<<<<<
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self._validate_attr(value, "height")
        self.__height = value

    # >>>>>>>>>>>>>>>>>>>   X   <<<<<<<<<<<<<<<<<<<<
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self._validate_attr(value, "x")
        self.__x = value

    # >>>>>>>>>>>>>>>>>>>   Y   <<<<<<<<<<<<<<<<<<<<
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self._validate_attr(value, "y")
        self.__y = value

    def _validate_attr(self, value: any, name: str):
        if not isinstance(value, int):
            err_msg = f"{name} must be an integer"
            raise TypeError(err_msg)

        if name in {"width", "height"} and value <= 0:
            err_msg = f"{name} must be > 0"
            raise ValueError(err_msg)

        if name in {"x", "y"} and value < 0:
            err_msg = f"{name} must be >= 0"
            raise ValueError(err_msg)

    def area(self):
        return self.__height * self.__width

    def display(self):
        for _ in range(self.__height):
            print("#" * self.__width)
