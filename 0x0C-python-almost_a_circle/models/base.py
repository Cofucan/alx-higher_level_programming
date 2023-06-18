#!/usr/bin/python3
"""
    Base Module
"""
import csv
import json
import os


class Base:
    """Base class which will be inherited by all other classes."""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries) -> str:
        """Serializes a list of dictionaries to JSON string.

        Args:
            list_dictionaries (list of dicts): List of dictionaries.

        Returns:
            str: JSON string representation of the list of dictionaries.
        """
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @staticmethod
    def from_json_string(json_string) -> any:
        """Deserializes a JSON string to Python object.

        Args:
            json_string (JSON str): The JSON string to deserialize.

        Returns:
            any: A Python object.
        """
        return json.loads(json_string) if json_string else []

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of `list_objs` to a file.

        Args:
            list_objs (list of objs): List of objects to be written.
        """
        filename = f"{cls.__name__}.json"
        with open(filename, mode="w", encoding="utf-8") as json_file:
            if not list_objs:
                json_file.write(cls.to_json_string([]))
            else:
                dict_objs = [obj.to_dictionary() for obj in list_objs]
                json_file.write(cls.to_json_string(dict_objs))

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with all attributes set.

        Args:
            dictionary: Dictionary of arguments to be used to create instance.

        Returns:
            object: An instance of a class that inherits from this class.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(8, 4)

        if cls.__name__ == "Square":
            dummy = cls(7)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls) -> list:
        """Reads data from a JSON file and creates instances with the data.

        Returns:
            list: A list of instances created using the read data.
        """
        filename = f"{cls.__name__}.json"
        if not os.path.isfile(filename):
            return []

        with open(filename, mode="r", encoding="utf-8") as json_file:
            instances = cls.from_json_string(json_file.read())

        return [cls.create(**instance) for instance in instances]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of objects to a CSV file.

        Args:
            list_objs (list): List of objects whose data is to be saved to CSV.
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, mode="w", encoding="utf-8") as csv_file:
            if cls.__name__ == "Rectangle":
                columns = ["id", "width", "height", "x", "y"]
            else:
                columns = ["id", "size", "x", "y"]

            writer = csv.DictWriter(csv_file, columns)
            writer.writerows([obj.to_dictionary() for obj in list_objs])

    @classmethod
    def load_from_file_csv(cls) -> list:
        """Deserializes a CSV file and uses the data to create new objects.

        Returns:
            list: List of objects created with the data read from the CSV.
        """
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
