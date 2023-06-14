#!/usr/bin/python3
"""Student Module"""


class Student:
    """Defines a Student class."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation of a Student instance."""
        if isinstance(attrs, list) and \
                (all(isinstance(s, str) for s in attrs)):
            return {k: v for k, v in dict(self.__dict__).items() if k in attrs}

        return self.__dict__

    def reload_from_json(self, json: dict):
        """Replaces all attributes of the Student instance."""
        (setattr(self, key, value) for key, value in json.items())
