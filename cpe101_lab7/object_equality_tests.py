import unittest
from objects import *

class MyTestCase(unittest.TestCase):
    def test_point_eq_1(self):
        point1: Point = Point(3, 1.1)
        point2: Point = Point(3.000000, 1.100000)
        self.assertEqual(point1, point2)  # add assertion here

    def test_point_eq_2(self):
        point1: Point = Point(-3, 1.1)
        point2: Point = Point(3.000000, 1.100000)
        self.assertNotEqual(point1, point2)


    def test_circle_eq_1(self):
        circle1: Circle = Circle(Point(0, 2), 5)
        circle2: Circle = Circle(Point(0, 2), 5)
        self.assertEqual(circle1, circle2)

    def test_circle_eq_2(self):
        circle1: Circle = Circle(Point(0.5, 2), 5)
        circle2: Circle = Circle(Point(0, 2), 5)
        self.assertNotEqual(circle1, circle2)

    def test_circle_eq_3(self):
        circle1: Circle = Circle(Point(0.5, -2), 50)
        circle2: Circle = Circle(Point(0.5, -2), 5)
        self.assertNotEqual(circle1, circle2)

if __name__ == '__main__':
    unittest.main()
