"""
Unit test documentation:
https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
"""

import unittest
import funcs

from unittest.mock import patch  # used to test when there are factors out of your code's control like a bad API request due to the server
# would use patch as a context manager, and then recreate the correct response from the API

class TestFuncs(unittest.TestCase):

    # these @classmethods run JUST ONCE at the very start and end of running the unit test module
    @classmethod
    def setUpClass(cls):
        print('SetupClass')

    @classmethod
    def tearDownClass(cls):
        print('TearDownClass')

    # this code runs before EVERY single test, like setting up objects used for testing in multiple test methods
    def setUp(self):
        self.x: int = 1  # have to do self.* so that way it's added to the TestFuncs class
        # then would have to use self.x in the test case methods

    # this method runs after every single test
    # same rules apply as setUp
    def tearDown(self):
        # could use for something like deleting/cleaning up files created by test methods
        pass

    # write all test methods so that they are independent of one another
    # all test methods need to be named test_* or the TestCase won't read
    # it when calling unittest.main()

    def test_f1(self):
        # assertEqual is one of the inherited methods from TestCase parent class
        result_f1 = funcs.f(1)
        self.assertEqual(result_f1, 9)  # add assertion here

    def test_f2(self):
        self.assertEqual(funcs.f(self.x), 9)  # add assertion here

    def test_f3(self):
        self.assertEqual(funcs.f(-3), 57), 'Something about negatives is off?'

    def test_f4(self):
        self.assertEqual(funcs.f(0), 0)


    def test_g1(self):
        with self.assertRaises(ZeroDivisionError):
            funcs.g(0, 3)

    def test_g2(self):
        self.assertAlmostEqual(funcs.g(3, 10), 12.1111111111111)

    def test_g3(self):
        self.assertAlmostEqual(funcs.g(-2, -4), -10/3)

    def test_g4(self):
        self.assertAlmostEqual(funcs.g(-5, 2), -1.933333333333)

    def test_hypotenuse1(self):
        self.assertAlmostEqual(funcs.hypotenuse(3, 4), 5)

    def test_hypotenuse2(self):
        self.assertAlmostEqual(funcs.hypotenuse(8, 3), 8.54400374531753)

    def test_is_positive1(self):
        self.assertTrue(funcs.is_positive(3))

    def test_is_positive2(self):
        self.assertFalse(funcs.is_positive(-4))

    def test_is_positive3(self):
        self.assertTrue(funcs.is_positive(0))


if __name__ == '__main__':
    unittest.main()
