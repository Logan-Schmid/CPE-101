import unittest
from fold_funcs import *

class MyTestCase(unittest.TestCase):
    def test_sum2_1(self):
        result: int = sum2([1, 4, -2, 1])
        self.assertEqual(result, 4)  # add assertion here

    def test_sum2_2(self):
        result: int = sum2([])
        self.assertEqual(result, 0)

    def test_sum2_3(self):
        result: int = sum2([-1010, -2, 0])
        self.assertEqual(result, -1012)


    def test_index_of_smallest_1(self):
        result: int = index_of_smallest([1, 4, -2, 1])
        self.assertEqual(result, 2)

    def test_index_of_smallest_2(self):
        result: int = index_of_smallest([])
        self.assertEqual(result, -1)

    def test_index_of_smallest_3(self):
        result: int = index_of_smallest([1])
        self.assertEqual(result, 0)

    def test_index_of_smallest_4(self):
        result: int = index_of_smallest([1, 3, 4, 5])
        self.assertEqual(result, 0)

    def test_index_of_smallest_5(self):
        result: int = index_of_smallest([9, 4, 3, 1])
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
