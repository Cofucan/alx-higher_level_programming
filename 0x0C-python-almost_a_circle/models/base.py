#!/usr/bin/python3
"""
    Base Module
"""
import csv
import json
import os


class Base:
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

    @staticmethod
    def from_json_string(json_string) -> list:
        return json.loads(json_string) if json_string else []

    @classmethod
    def save_to_file(cls, list_objs):
        filename = f"{cls.__name__}.json"
        with open(filename, mode="w", encoding="utf-8") as s:
            if not list_objs:
                s.write(cls.to_json_string([]))
            else:
                dict_objs = [obj.to_dictionary() for obj in list_objs]
                s.write(cls.to_json_string(dict_objs))

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(8, 4)

        if cls.__name__ == "Square":
            dummy = cls(7)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = f"{cls.__name__}.json"
        if not os.path.isfile(filename):
            return []

        with open(filename, mode="r", encoding="utf-8") as s:
            instances = cls.from_json_string(s.read())

        return [cls.create(**instance) for instance in instances]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = f"{cls.__name__}.csv"
        with open(filename, mode="w", encoding="utf-8") as csv_file:
            if cls.__name__ == "Rectangle":
                columns = ["id", "width", "height", "x", "y"]
            else:
                columns = ["id", "size", "x", "y"]

            writer = csv.DictWriter(csv_file, columns)
            writer.writerows([obj.to_dictionary() for obj in list_objs])

    @classmethod
    def load_from_file_csv(cls):
        filename = f"{cls.__name__}.csv"

        try:
            with open(filename, mode="r", encoding="utf-8") as csv_file:
                if cls.__name__ == "Rectangle":
                    columns = ["id", "width", "height", "x", "y"]
                else:
                    columns = ["id", "size", "x", "y"]

                reader = csv.DictReader(csv_file, columns)
                reader = [{key: int(value) for key, value in row.items()}
                          for row in reader]
                return [cls.create(**(args)) for args in reader]
        except IOError:
            return []
