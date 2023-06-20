#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def setUp(self):
        """Set up the test fixture."""
        self.rectangle = Rectangle(5, 10, 1, 2, 100)

    def test_constructor(self):
        """Test the constructor of the Rectangle class."""
        self.assertEqual(self.rectangle.width, 5)
        self.assertEqual(self.rectangle.height, 10)
        self.assertEqual(self.rectangle.x, 1)
        self.assertEqual(self.rectangle.y, 2)
        self.assertEqual(self.rectangle.id, 100)

    def test_set_width(self):
        """Test setting the width of the rectangle."""
        self.rectangle.width = 8
        self.assertEqual(self.rectangle.width, 8)

    def test_set_height(self):
        """Test setting the height of the rectangle."""
        self.rectangle.height = 15
        self.assertEqual(self.rectangle.height, 15)

    def test_set_x(self):
        """Test setting the x-coordinate of the rectangle's position."""
        self.rectangle.x = 3
        self.assertEqual(self.rectangle.x, 3)

    def test_set_y(self):
        """Test setting the y-coordinate of the rectangle's position."""
        self.rectangle.y = 4
        self.assertEqual(self.rectangle.y, 4)

    def test_area(self):
        """Test calculating the area of the rectangle."""
        self.assertEqual(self.rectangle.area(), 50)

    def test_display(self):
        """Test displaying the rectangle."""
        # Not easily testable, manual inspection required
        self.rectangle.display()

    def test_to_dictionary(self):
        """Test converting the rectangle to a dictionary."""
        expected_dict = {
            "id": 100,
            "width": 5,
            "height": 10,
            "x": 1,
            "y": 2
        }
        self.assertEqual(self.rectangle.to_dictionary(), expected_dict)

    def test_update_with_args(self):
        """Test updating the rectangle's attributes with positional arguments."""
        self.rectangle.update(7, 12, 2, 3, 200)
        self.assertEqual(self.rectangle.width, 12)
        self.assertEqual(self.rectangle.height, 2)
        self.assertEqual(self.rectangle.x, 3)
        self.assertEqual(self.rectangle.y, 200)
        self.assertEqual(self.rectangle.id, 7)

    def test_update_with_kwargs(self):
        """Test updating the rectangle's attributes with keyword arguments."""
        self.rectangle.update(width=8, height=15, x=3, y=4, id=300)
        self.assertEqual(self.rectangle.width, 8)
        self.assertEqual(self.rectangle.height, 15)
        self.assertEqual(self.rectangle.x, 3)
        self.assertEqual(self.rectangle.y, 4)
        self.assertEqual(self.rectangle.id, 300)

    def test_str(self):
        """Test the string representation of the rectangle."""
        expected_str = "[Rectangle] (100) 1/2 - 5/10"
        self.assertEqual(str(self.rectangle), expected_str)


if __name__ == "__main__":
    unittest.main()
