import unittest
from poly import poly_add2, poly_mult2

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

    def test_poly_add2_1(self):
        poly1: list[float] = [2, 4, 5]
        poly2: list[float] = [4, 0, 1]
        result: list[float] = poly_add2(poly1, poly2)
        self.assert_list_almost_equal(result, [6, 4, 6])

    def test_poly_add2_2(self):
        poly1: list[float] = [0, 4, -5]
        poly2: list[float] = [-1, 4]
        result: list[float] = poly_add2(poly1, poly2)
        self.assert_list_almost_equal(result, [-1, 8, -5])

    def test_poly_add2_3(self):
        poly1: list[float] = []
        poly2: list[float] = [-1, 4, 5, 0, 2]
        result: list[float] = poly_add2(poly1, poly2)
        self.assert_list_almost_equal(result, [-1, 4, 5, 0, 2])


    def test_poly_mult2_1(self):
        poly1: list[float] = [2, 4, 5]
        poly2: list[float] = [4, 0, 1]
        result: list[float] = poly_mult2(poly1, poly2)
        self.assert_list_almost_equal(result, [8, 16, 22, 4, 5])  # add assertion here

    def test_poly_mult2_2(self):
        poly1: list[float] = []
        poly2: list[float] = []
        result: list[float] = poly_mult2(poly1, poly2)
        self.assert_list_almost_equal(result, [])

    def test_poly_mult2_3(self):
        poly1: list[float] = [2]
        poly2: list[float] = [-4]
        result: list[float] = poly_mult2(poly1, poly2)
        self.assert_list_almost_equal(result, [-8])

    def test_poly_mult2_4(self):
        poly1: list[float] = [-1, 4]
        poly2: list[float] = [4, -3, -7]
        result: list[float] = poly_mult2(poly1, poly2)
        self.assert_list_almost_equal(result, [-4, 19, -5, -28])


if __name__ == '__main__':
    unittest.main()
