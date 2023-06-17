#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rect = Rectangle(5, 10, 2, 3)

    def test_width(self):
        self.assertEqual(self.rect.width, 5)
        self.rect.width = 13
        self.assertEqual(self.rect.width, 13)

    def test_height(self):
        self.assertEqual(self.rect.height, 10)
        self.rect.height = 61
        self.assertEqual(self.rect.height, 61)

    def test_x(self):
        self.assertEqual(self.rect.x, 2)
        self.rect.x = 9
        self.assertEqual(self.rect.x, 9)

    def test_y(self):
        self.assertEqual(self.rect.y, 3)
        self.rect.y = 24
        self.assertEqual(self.rect.y, 24)

    def test_area(self):
        self.assertEqual(self.rect.area(), 50)

    def test_display(self):
        self.rect.display()
        # Output:
        # #####
        # #####
        # #####
        # #####
        # #####
        # #####
        # #####
        # #####
        # #####
        # #####

    def test_str(self):
        self.assertEqual(str(self.rect), "[Rectangle] (4) 2/3 - 5/10")


if __name__ == '__main__':
    unittest.main()
