import unittest
from rectangle import Rectangle

class TestGetAreaRectangle(unittest.TestCase):
    def test_normal_case(self):
        rectangle = Rectangle(2,3)
        self.assertEqual(rectangle.get_area(), 6, "incorrect area")

    def test_negative_case(self):
        rectangle = Rectangle(-1, 2)
        self.assertEqual(rectangle.get_area(), -1, "incorrect negative output")

unittest.main()
