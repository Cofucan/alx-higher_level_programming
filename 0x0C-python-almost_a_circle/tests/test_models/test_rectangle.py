#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rect = Rectangle(5, 10, 2, 3)

    # def tearDown(self):
    #     del self.rect

    def test_1_width(self):
        self.assertEqual(self.rect.width, 5)
        self.rect.width = 13
        self.assertEqual(self.rect.width, 13)

    def test_2_height(self):
        self.assertEqual(self.rect.height, 10)
        self.rect.height = 61
        self.assertEqual(self.rect.height, 61)

    def test_3_x(self):
        self.assertEqual(self.rect.x, 2)
        self.rect.x = 9
        self.assertEqual(self.rect.x, 9)

    def test_4_y(self):
        self.assertEqual(self.rect.y, 3)
        self.rect.y = 24
        self.assertEqual(self.rect.y, 24)

    def test_5_area(self):
        self.assertEqual(self.rect.area(), 50)

    def test_6_display(self):
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

    # def test_7_str(self):
    #     self.assertEqual(str(self.rect), "[Rectangle] (11) 2/3 - 5/10")


if __name__ == '__main__':
    unittest.main()
