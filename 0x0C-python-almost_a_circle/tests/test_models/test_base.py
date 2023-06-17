#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_init_with_id(self):
        b = Base(123)
        self.assertEqual(b.id, 123)

    def test_init_without_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_multiple_instances(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(456)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 456)


if __name__ == '__main__':
    unittest.main()