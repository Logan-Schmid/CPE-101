import unittest
from list_comp import *
from math import sqrt

class CustomAssertion:
    @staticmethod
    def almost_equal(num1: float, num2: float) -> bool:
        abs_dif = abs(num1 - num2)
        tolerance: float = 1e-7
        return abs_dif < tolerance

    def assert_list_almost_equal(self, list1: list, list2: list) -> None:
        if len(list1) != len(list2):
            # print('lengths are different!')
            raise AssertionError(f'{list1} ~!= {list2}')

        for i in range(len(list1)):
            if not self.almost_equal(list1[i], list2[i]):
                # print(f'{self} failed: was not almost equal')
                raise AssertionError(f'{list1} ~!= {list2}')

class MyTestCase(unittest.TestCase, CustomAssertion):
    def test_distance_all_1(self):
        points: list[Point] = []
        distances: list[float] = distance_all(points)
        self.assertListEqual(distances, [])  # add assertion here

    def test_distance_all_2(self):
        points: list[Point] = [Point(2, 2), Point(5, -12)]
        distances: list[float] = distance_all(points)
        self.assert_list_almost_equal(distances, [sqrt(8), 13])


    def test_are_in_first_quadrant_1(self):
        points: list[Point] = [Point(2, 2), Point(5, -12)]
        in_first_quadrant: list[Point] = are_in_first_quadrant(points)
        self.assertListEqual(in_first_quadrant, [Point(2, 2)])

    def test_are_in_first_quadrant_2(self):
        points: list[Point] = [Point(0, 0), Point(-3, -12), Point(-1,0)]
        in_first_quadrant: list[Point] = are_in_first_quadrant(points)
        self.assertListEqual(in_first_quadrant, [Point(0, 0)])

    def test_are_in_first_quadrant_3(self):
        points: list[Point] = []
        in_first_quadrant: list[Point] = are_in_first_quadrant(points)
        self.assertListEqual(in_first_quadrant, [])

if __name__ == '__main__':
    unittest.main()
