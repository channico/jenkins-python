# tests/test_my_class.py

import unittest
from my_module.my_class import MyClass


class TestMyClass(unittest.TestCase):
    def setUp(self):
        self.my_class = MyClass("World")

    def test_greet(self):
        self.assertEqual(self.my_class.greet(), "Hello, World!")

    def test_add(self):
        self.assertEqual(self.my_class.add(1, 2), 3)
        self.assertEqual(self.my_class.add(-1, 1), 0)
        self.assertEqual(self.my_class.add(-1, -1), -2)


if __name__ == '__main__':
    unittest.main()
