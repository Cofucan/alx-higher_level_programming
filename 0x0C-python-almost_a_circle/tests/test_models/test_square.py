#!/usr/bin/python3

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def setUp(self):
        """Set up the test fixture."""
        self.square = Square(5, 1, 2, 100)

    def test_constructor(self):
        """Test the constructor of the Square class."""
        self.assertEqual(self.square.size, 5)
        self.assertEqual(self.square.width, 5)
        self.assertEqual(self.square.height, 5)
        self.assertEqual(self.square.x, 1)
        self.assertEqual(self.square.y, 2)
        self.assertEqual(self.square.id, 100)

    def test_set_size(self):
        """Test setting the size of the square."""
        self.square.size = 8
        self.assertEqual(self.square.size, 8)
        self.assertEqual(self.square.width, 8)
        self.assertEqual(self.square.height, 8)

    def test_update_with_args(self):
        """Test updating the square's attributes with positional arguments."""
        self.square.update(200, 7, 2, 3)
        self.assertEqual(self.square.size, 7)
        self.assertEqual(self.square.width, 7)
        self.assertEqual(self.square.height, 7)
        self.assertEqual(self.square.x, 2)
        self.assertEqual(self.square.y, 3)
        self.assertEqual(self.square.id, 200)

    def test_update_with_kwargs(self):
        """Test updating the square's attributes with keyword arguments."""
        self.square.update(size=8, x=3, y=4, id=300)
        self.assertEqual(self.square.size, 8)
        self.assertEqual(self.square.width, 8)
        self.assertEqual(self.square.height, 8)
        self.assertEqual(self.square.x, 3)
        self.assertEqual(self.square.y, 4)
        self.assertEqual(self.square.id, 300)

    def test_to_dictionary(self):
        """Test converting the square to a dictionary."""
        expected_dict = {
            "id": 100,
            "size": 5,
            "x": 1,
            "y": 2
        }
        self.assertEqual(self.square.to_dictionary(), expected_dict)

    def test_str(self):
        """Test the string representation of the square."""
        expected_str = "[Square] (100) 1/2 - 5"
        self.assertEqual(str(self.square), expected_str)


if __name__ == '__main__':
    unittest.main()
