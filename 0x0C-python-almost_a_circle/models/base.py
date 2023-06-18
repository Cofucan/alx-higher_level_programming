#!/usr/bin/python3
"""
    Base Module
"""
import json


class Base():
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries) -> str:
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        filename = f"{cls.__name__}.json"
        with open(filename, mode="w", encoding="utf-8") as s:
            if not list_objs:
                s.write(cls.to_json_string([]))
            else:
                dict_objs = [obj.to_dictionary() for obj in list_objs]
                s.write(cls.to_json_string(dict_objs))
