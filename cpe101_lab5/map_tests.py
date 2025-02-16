import unittest
from map_funcs import *

class MyTestCase(unittest.TestCase):
    def test_square_all_1(self):
        my_list: list[int] = square_all([1, 4, 9, 16])
        self.assertListEqual(my_list, [1, 16, 81, 256])  # add assertion here

    def test_square_all_2(self):
        my_list: list[int] = square_all([])
        self.assertListEqual(my_list, [])

    def test_square_all_3(self):
        my_list: list[int] = square_all([0])
        self.assertListEqual(my_list, [0])

    def test_square_all_4(self):
        my_list: list[int] = square_all([-1, 0, -3, 2])
        self.assertListEqual(my_list, [1, 0, 9, 4])


    def test_add_n_all_1(self):
        my_list: list[int] = add_n_all([-1, 0, -3, 2], 3)
        self.assertListEqual(my_list, [2, 3, 0, 5])

    def test_add_n_all_2(self):
        my_list: list[int] = add_n_all([0], -1)
        self.assertListEqual(my_list, [-1])

    def test_add_n_all_3(self):
        my_list: list[int] = add_n_all([], 3)
        self.assertListEqual(my_list, [])


    def test_even_or_odd_all_1(self):
        my_list: list[bool] = even_or_odd_all([-1, 0, -3, 2])
        self.assertListEqual(my_list, [False, True, False, True])

    def test_even_or_odd_all_2(self):
        my_list: list[bool] = even_or_odd_all([])
        self.assertListEqual(my_list, [])

    def test_even_or_odd_all_3(self):
        my_list: list[bool] = even_or_odd_all([-5, -10, 9])
        self.assertListEqual(my_list, [0, 1, 0])

if __name__ == '__main__':
    unittest.main()
