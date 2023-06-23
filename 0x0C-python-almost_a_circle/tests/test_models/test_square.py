#!/usr/bin/python3
"""
A module that test differents behaviors
of the Square class
"""
import unittest
from models.base import Base
from models.square import Square
from pathlib import Path


class TestSquare(unittest.TestCase):
    """Unit tests for testing the Square class."""

    def test_getter(self):
        """Test the getter method of Square."""
        square = Square(5)
        self.assertEqual(square.size, 5)

    def test_setter(self):
        """Test the setter method of Square."""
        square = Square(5)
        square.size = 8
        self.assertEqual(square.size, 8)

    def test_string(self):
        """Test setting size with a string value."""
        square = Square(3)
        with self.assertRaises(TypeError):
            square.size = "Hi"

    def test_negative(self):
        """Test setting size with a negative value."""
        square = Square(6)
        with self.assertRaises(ValueError):
            square.size = -5

    def test_zero(self):
        """Test setting size with zero."""
        square = Square(6)
        with self.assertRaises(ValueError):
            square.size = 0

    def test_decimal(self):
        """Test setting size with a decimal value."""
        square = Square(6)
        with self.assertRaises(TypeError):
            square.size = 1.5

    def test_tuple(self):
        """Test setting size with a tuple value."""
        square = Square(7)
        with self.assertRaises(TypeError):
            square.size = (2, 8)

    def test_empty(self):
        """Test setting size with an empty value."""
        square = Square(7)
        with self.assertRaises(TypeError):
            square.size = ""

    def test_none(self):
        """Test setting size with None."""
        square = Square(5)
        with self.assertRaises(TypeError):
            square.size = None

    def test_list(self):
        """Test setting size with a list value."""
        square = Square(4)
        with self.assertRaises(TypeError):
            square.size = [4, 7]

    def test_dict(self):
        """Test setting size with a dictionary value."""
        square = Square(5)
        with self.assertRaises(TypeError):
            square.size = {"hi": 5, "world": 8}

    def test_width(self):
        """Test if width and height are updated when setting size."""
        square = Square(5)
        square.size = 6
        self.assertEqual(square.width, 6)
        self.assertEqual(square.height, 6)

    def test_to_dictionary(self):
        """Test the to_dictionary method of Square."""
        Base._Base__nb_objects = 0

        square = Square(10, 2, 1, 9)
        square_dict = square.to_dictionary()
        expected = {"id": 9, "x": 2, "size": 10, "y": 1}
        self.assertEqual(square_dict, expected)

        square = Square(1, 0, 0, 9)
        square_dict = square.to_dictionary()
        expected = {"id": 9, "x": 0, "size": 1, "y": 0}
        self.assertEqual(square_dict, expected)

        square.update(5, 5, 5, 5)
        square_dict = square.to_dictionary()
        expected = {"id": 5, "x": 5, "size": 5, "y": 5}
        self.assertEqual(square_dict, expected)


class TestSquareCreate(unittest.TestCase):
    """
    Test if the create method returns a new Square instance
    with the attributes updated.
    """

    def test_square_create_1_arg(self):
        """
        Test if the create method returns a Square instance with
        the one attribute updated.
        """
        sqr = Square.create(**{"id": 6})
        self.assertEqual(sqr.id, 6)

    def test_square_create_2_args(self):
        """
        Test if the create method returns a Square instance with
        two attributes updated.
        """
        sqr = Square.create(**{"id": 6, "size": 7})
        self.assertEqual(sqr.id, 6)
        self.assertEqual(sqr.size, 7)

    def test_square_create_3_args(self):
        """
        Test if the create method returns a Square instance with
        three attributes updated.
        """
        sqr = Square.create(**{"id": 6, "size": 7, "x": 8})
        self.assertEqual(sqr.id, 6)
        self.assertEqual(sqr.size, 7)
        self.assertEqual(sqr.x, 8)

    def test_square_create_4_args(self):
        """
        Test if the create method returns a Square instance with
        four attributes updated.
        """
        sqr = Square.create(**{"id": 6, "size": 7, "x": 8, "y": 9})
        self.assertEqual(sqr.id, 6)
        self.assertEqual(sqr.size, 7)
        self.assertEqual(sqr.x, 8)
        self.assertEqual(sqr.y, 9)


class TestSquareSaveToFile(unittest.TestCase):
    """Unit tests for testing the save_to_file method of Square."""

    def test_rectangle_save_to_file(self):
        """
        Test the save_to_file method with default.
        """
        Square.save_to_file(None)
        objs = Square.load_from_file()
        self.assertEqual(len(objs), 0)

    def test_square_save_to_file(self):
        """
        Test method for testing the save_to_file method with nothing.
        """
        Square.save_to_file([])
        objs = Square.load_from_file()
        self.assertEqual(len(objs), 0)

    def test_square_save_to_file_2(self):
        """
        Test method for testing the save_to_file method with a list.
        """
        Square.save_to_file([Square(1, 2, 3, 4)])
        objs = Square.load_from_file()
        self.assertEqual(len(objs), 1)
        self.assertIsInstance(objs[0], Square)
        self.assertEqual(objs[0].id, 4)
        self.assertEqual(objs[0].x, 2)
        self.assertEqual(objs[0].y, 3)
        self.assertEqual(objs[0].size, 1)


class TestSquareLoadFromFile(unittest.TestCase):
    """Unit tests for testing the load_from_file method of Square."""

    def setUp(self):
        """
        Removes the Square.json file if it exists.
        """
        if Path("Square.json").is_file():
            Path("Square.json").unlink()

    def test_square_load_from_file_no_file(self):
        """
        Test the load_from_file method with missing Square.json file.
        """
        self.assertFalse(Path("Square.json").is_file())
        self.assertEqual(Square.load_from_file(), [])

    def test_square_load_from_existing_file(self):
        """
        Test the load_from_file method with existing Square.json file.
        """
        Square.save_to_file([Square(1, 2, 3, 4)])
        objs = Square.load_from_file()
        self.assertEqual(len(objs), 1)
        self.assertIsInstance(objs[0], Square)
        self.assertEqual(objs[0].id, 4)
        self.assertEqual(objs[0].x, 2)
        self.assertEqual(objs[0].y, 3)
        self.assertEqual(objs[0].size, 1)


if __name__ == "__main__":
    unittest.main()
