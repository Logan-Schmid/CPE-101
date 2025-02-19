import unittest
import logic

class MyTestCase(unittest.TestCase):
    def test_is_even1(self):
        self.assertTrue(logic.is_even(0))  # add assertion here

    def test_is_even2(self):
        self.assertFalse(logic.is_even(1))

    def test_is_even3(self):
        self.assertTrue(logic.is_even(-4))

    def test_is_even4(self):
        self.assertFalse(logic.is_even(-3))

    def test_is_even5(self):
        self.assertTrue(logic.is_even(6))


    def test_is_an_interval1(self):
        self.assertFalse(logic.is_an_interval(1))

    def test_is_an_interval2(self):
        self.assertFalse(logic.is_an_interval(9))

    def test_is_an_interval3(self):
        self.assertFalse(logic.is_an_interval(47))

    def test_is_an_interval4(self):
        self.assertFalse(logic.is_an_interval(92))

    def test_is_an_interval5(self):
        self.assertFalse(logic.is_an_interval(12))

    def test_is_an_interval6(self):
        self.assertFalse(logic.is_an_interval(30))

    def test_is_an_interval7(self):
        self.assertFalse(logic.is_an_interval(100))

    def test_is_an_interval8(self):
        self.assertTrue(logic.is_an_interval(2))

    def test_is_an_interval9(self):
        self.assertTrue(logic.is_an_interval(7))

    def test_is_an_interval10(self):
        self.assertTrue(logic.is_an_interval(101))




if __name__ == '__main__':
    unittest.main()
