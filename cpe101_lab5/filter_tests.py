import unittest
from filter_funcs import *

class MyTestCase(unittest.TestCase):
    def test_are_positive_1(self):
        my_list: list[int] = are_positive([0, 3, 2, -1, -4, 1])
        self.assertListEqual(my_list, [0, 3, 2, 1])  # add assertion here

    def test_are_positive_2(self):
        my_list: list[int] = are_positive([-2, -1, -10])
        self.assertListEqual(my_list, [])


    def test_are_greater_than_n_1(self):
        my_list: list[int] = are_greater_than_n([-2, -1, -10], -1)
        self.assertListEqual(my_list, [])

    def test_are_greater_than_n_2(self):
        my_list: list[int] = are_greater_than_n([-2, -1, -10], -5)
        self.assertListEqual(my_list, [-2, -1])

    def test_are_greater_than_n_3(self):
        my_list: list[int] = are_greater_than_n([], -1)
        self.assertListEqual(my_list, [])

    def test_are_greater_than_n_4(self):
        my_list: list[int] = are_greater_than_n([1, 4, 9], 0)
        self.assertListEqual(my_list, [1, 4, 9])


    def test_are_divisible_by_n_1(self):
        my_list: list[int] = are_divisible_by_n([-2, -1, -10], 2)
        self.assertListEqual(my_list, [-2, -10])

    def test_are_divisible_by_n_2(self):
        my_list: list[int] = are_divisible_by_n([], 2)
        self.assertListEqual(my_list, [])

    def test_are_divisible_by_n_3(self):
        my_list: list[int] = are_divisible_by_n([3, -1, 0, 9, -12], 3)
        self.assertListEqual(my_list, [3, 0, 9, -12])

if __name__ == '__main__':
    unittest.main()
