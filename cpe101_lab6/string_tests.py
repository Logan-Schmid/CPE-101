import unittest

from cpe101_lab6.string_funcs import str_rot_13, str_translate_101


class MyTestCase(unittest.TestCase):
    def test_str_rot_13_1(self):
        self.assertEqual(str_rot_13('abcde'), 'nopqr')

    def test_str_rot_13_2(self):
        self.assertEqual(str_rot_13('noz'), 'abm')

    def test_str_rot_13_3(self):
        self.assertEqual(str_rot_13(''), '')

    def test_str_rot_13_4(self):
        self.assertEqual(str_rot_13('a034 e'), 'n034 r')

    def test_str_rot_13_5(self):
        self.assertEqual(str_rot_13('abcde'.upper()), 'nopqr'.upper())

    def test_str_rot_13_6(self):
        self.assertEqual(str_rot_13('NOZ'), 'ABM')


    def test_str_translate_101_1(self):
        result: str = str_translate_101('abrgw', 'r', 'X')
        self.assertEqual(result, 'abXgw')

    def test_str_translate_101_2(self):
        result: str = str_translate_101('', 'r', 'X')
        self.assertEqual(result, '')

    def test_str_translate_101_3(self):
        result: str = str_translate_101('23840', '2', 'x')
        self.assertEqual(result, 'x3840')

    def test_str_translate_101_4(self):
        result: str = str_translate_101('     ', ' ', '_')
        self.assertEqual(result, '_____')

if __name__ == '__main__':
    unittest.main()
