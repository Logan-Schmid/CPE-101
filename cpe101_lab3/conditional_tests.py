import unittest
from conditional import max_101, max_of_three, rental_late_fee

class MyTestCase(unittest.TestCase):
    def test_max_101_1(self):
        self.assertEqual(max_101(2, 4), 4)  # add assertion here

    def test_max_101_2(self):
        self.assertEqual(max_101(3, 3), 3)

    def test_max_101_3(self):
        self.assertEqual(max_101(-5, -9), -5)

    def test_max_101_4(self):
        self.assertEqual(max_101(1, -3), 1)


    def test_max_of_three_1(self):
        self.assertEqual(max_of_three(1,1,1), 1)

    def test_max_of_three_2(self):
        self.assertEqual(max_of_three(1,3,1), 3)

    def test_max_of_three_3(self):
        self.assertEqual(max_of_three(3,3,1), 3)

    def test_max_of_three_4(self):
        self.assertEqual(max_of_three(-5, -6, -4), -4)

    def test_max_of_three_5(self):
        self.assertEqual(max_of_three(4,1,4), 4)

    def test_max_of_three_6(self):
        self.assertEqual(max_of_three(-2,-2,3), 3)


    def test_rental_late_fee_1(self):
        self.assertEqual(rental_late_fee(100), 100)

    def test_rental_late_fee_2(self):
        self.assertEqual(rental_late_fee(24), 19)

    def test_rental_late_fee_3(self):
        self.assertEqual(rental_late_fee(16), 19)

    def test_rental_late_fee_4(self):
        self.assertEqual(rental_late_fee(15), 7)

    def test_rental_late_fee_5(self):
        self.assertEqual(rental_late_fee(11), 7)

    def test_rental_late_fee_6(self):
        self.assertEqual(rental_late_fee(9), 5)

    def test_rental_late_fee_7(self):
        self.assertEqual(rental_late_fee(6), 5)

    def test_rental_late_fee_8(self):
        self.assertEqual(rental_late_fee(0), 0)

    def test_rental_late_fee_9(self):
        self.assertEqual(rental_late_fee(-5), 0)


if __name__ == '__main__':
    unittest.main()
