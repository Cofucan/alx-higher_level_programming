#!/usr/bin/python3
"""
    Square Module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        self._validate_attr(size, "size")
        self._validate_attr(x, "x")
        self._validate_attr(y, "y")
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
