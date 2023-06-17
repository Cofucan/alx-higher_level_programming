#!/usr/bin/python3
"""
    Square Module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        self._validate_attr(size, "width")
        self._validate_attr(x, "x")
        self._validate_attr(y, "y")
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self._validate_attr(value, "width")
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
