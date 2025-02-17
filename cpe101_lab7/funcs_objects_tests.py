import unittest
from objects import *
from funcs_objects import *

class MyTestCase(unittest.TestCase):
    def test_Point_1(self):
        my_point: Point = Point(1.2, -5)
        self.assertAlmostEqual(my_point.x, 1.2)  # add assertion here
        self.assertAlmostEqual(my_point.y, -5)  # add assertion here

    def test_Point_2(self):
        my_point: Point = Point(0, 0)
        self.assertAlmostEqual(my_point.x, 0)  # add assertion here
        self.assertAlmostEqual(my_point.y, 0)  # add assertion here


    def test_Circle_1(self):
        my_circle: Circle = Circle(Point(1, -3), 4.1)
        self.assertAlmostEqual(my_circle.center.x, 1)
        self.assertAlmostEqual(my_circle.center.y, -3)
        self.assertAlmostEqual(my_circle.radius, 4.1)

    def test_Circle_2(self):
        my_circle: Circle = Circle(Point(-0.1, 0.1100), 0)
        self.assertAlmostEqual(my_circle.center.x, -0.1)
        self.assertAlmostEqual(my_circle.center.y, 0.1100)
        self.assertAlmostEqual(my_circle.radius, 0)


    def test_distance_1(self):
        point1: Point = Point(3, 9)
        point2: Point = Point(-2, 0)
        result: float = distance(point1, point2)
        self.assertAlmostEqual(result, 10.295630141)

    def test_distance_2(self):
        point1: Point = Point(0, 5)
        point2: Point = Point(0, 5)
        result: float = distance(point1, point2)
        self.assertAlmostEqual(result, 0)

    def test_distance_3(self):
        point1: Point = Point(-1, 0)
        point2: Point = Point(-6, 12)
        result: float = distance(point1, point2)
        self.assertAlmostEqual(result, 13)


    def test_circles_overlap_1(self):
        circle1: Circle = Circle(Point(-1, 0), 2)
        circle2: Circle = Circle(Point(3, 0), 2)
        result: bool = circles_overlap(circle1, circle2)
        self.assertFalse(result)

    def test_circles_overlap_2(self):
        circle1: Circle = Circle(Point(1, -3), 3)
        circle2: Circle = Circle(Point(-4, 3), 5)
        result: bool = circles_overlap(circle1, circle2)
        self.assertTrue(result)

    def test_circles_overlap_3(self):
        circle1: Circle = Circle(Point(0, 0), 0)
        circle2: Circle = Circle(Point(0, 0), 0)
        result: bool = circles_overlap(circle1, circle2)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
