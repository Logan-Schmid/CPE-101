import unittest
from funcs import pounds_to_kg, get_mass_object, get_velocity_object, get_velocity_skater

class MyTestCase(unittest.TestCase):
    def test_pounds_to_kg_1(self):
        result: float = pounds_to_kg(100)
        self.assertAlmostEqual(result, 45.3592)  # add assertion here

    def test_pounds_to_kg_2(self):
        result: float = pounds_to_kg(0)
        self.assertAlmostEqual(result, 0)

    def test_pounds_to_kg_3(self):
        with self.assertRaises(ValueError) as context:
            result = pounds_to_kg(-1)

        self.assertTrue('Weight cannot be negative!' in str(context.exception))


    def test_get_mass_object_1(self):
        result: float = get_mass_object('t')
        self.assertAlmostEqual(result, 0.1)

    def test_get_mass_object_2(self):
        result: float = get_mass_object('p')
        self.assertAlmostEqual(result, 1.0)

    def test_get_mass_object_3(self):
        result: float = get_mass_object('r')
        self.assertAlmostEqual(result, 3.0)

    def test_get_mass_object_4(self):
        result: float = get_mass_object('g')
        self.assertAlmostEqual(result, 5.3)

    def test_get_mass_object_5(self):
        result: float = get_mass_object('l')
        self.assertAlmostEqual(result, 9.07)

    def test_get_mass_object_6(self):
        result: float = get_mass_object('z')
        self.assertAlmostEqual(result, 0.0)

    def test_get_mass_object_7(self):
        result: float = get_mass_object(0)
        self.assertAlmostEqual(result, 0.0)


    def test_get_velocity_object_1(self):
        result: float = get_velocity_object(3)
        self.assertAlmostEqual(result, 3.8340579025361627)

    def test_get_velocity_object_2(self):
        result: float = get_velocity_object(0)
        self.assertAlmostEqual(result, 0)


    def test_get_velocity_skater_1(self):
        result: float = get_velocity_skater(3, 2, 5)
        self.assertAlmostEqual(result,3.3333333333333333)

    def test_get_velocity_skater_2(self):
        with self.assertRaises(ValueError) as context:
            result = get_velocity_skater(-1, 1, 10)

        self.assertTrue('Masses cannot be negative!' in str(context.exception))

    def test_get_velocity_skater_3(self):
        with self.assertRaises(ValueError) as context:
            result = get_velocity_skater(1, -1, 10)

        self.assertTrue('Masses cannot be negative!' in str(context.exception))

    def test_get_velocity_skater_4(self):
        with self.assertRaises(ZeroDivisionError) as context:
            result = get_velocity_skater(0, 1, 10)

if __name__ == '__main__':
    unittest.main()
