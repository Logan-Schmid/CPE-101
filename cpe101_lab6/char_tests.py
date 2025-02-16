import unittest
from char_funcs import *

class MyTestCase(unittest.TestCase):
    def test_is_lower_101_1(self):
        self.assertFalse(is_lower_101('Z'))  # add assertion here

    def test_is_lower_101_2(self):
        self.assertFalse(is_lower_101('B'))

    def test_is_lower_101_3(self):
        self.assertTrue(is_lower_101('f'))

    def test_is_lower_101_4(self):
        self.assertTrue(is_lower_101('a'))

    def test_is_lower_101_5(self):
        self.assertTrue(is_lower_101('z'))

    def test_is_lower_101_6(self):
        self.assertFalse(is_lower_101(''))

    def test_is_lower_101_7(self):
        self.assertFalse(is_lower_101('0'))


    def test_char_rot_13_1(self):
        self.assertEqual(char_rot_13('a'), 'n')

    def test_char_rot_13_2(self):
        self.assertEqual(char_rot_13('b'), 'o')

    def test_char_rot_13_3(self):
        self.assertEqual(char_rot_13('n'), 'a')

    def test_char_rot_13_4(self):
        self.assertEqual(char_rot_13('A'), 'N')

    def test_char_rot_13_5(self):
        self.assertEqual(char_rot_13('N'), 'A')

    def test_char_rot_13_6(self):
        self.assertEqual(char_rot_13('Z'), 'M')

    def test_char_rot_13_7(self):
        self.assertEqual(char_rot_13('9'), '9')

    def test_char_rot_13_8(self):
        self.assertEqual(char_rot_13(''), '')

    def test_char_rot_13_9(self):
        self.assertEqual(char_rot_13('/'), '/')

    def test_char_rot_13_10(self):
        self.assertEqual(char_rot_13(' '), ' ')




if __name__ == '__main__':
    unittest.main()
