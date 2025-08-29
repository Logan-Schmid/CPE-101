import unittest
from lander_funcs import update_fuel, update_altitude, update_acceleration, update_velocity

class TestCalculateFuncs(unittest.TestCase):
    def test_update_acceleration_1(self):
        my_accel: float = update_acceleration(1.62, 5)
        self.assertAlmostEqual(0.0, my_accel)  # add assertion here

    def test_update_acceleration_2(self):
        my_accel: float = update_acceleration(1.62, 0)
        self.assertAlmostEqual(-1.62, my_accel)

    def test_update_acceleration_3(self):
        my_accel: float = update_acceleration(9.81, 9)
        self.assertAlmostEqual(7.848, my_accel)


    def test_update_altitude_1(self):
        my_vel: float = update_altitude(1000, -4, -1.62)
        self.assertAlmostEqual(995.19, my_vel)

    def test_update_altitude_2(self):
        my_vel: float = update_altitude(3, -5, 0)
        self.assertAlmostEqual(0.0, my_vel)


    def test_update_velocity_1(self):
        my_vel: float = update_velocity(-5, -1)
        self.assertAlmostEqual(-6.0, my_vel)

    def test_update_velocity_2(self):
        my_vel: float = update_velocity(-1, 0)
        self.assertAlmostEqual(-1.0, my_vel)


    def test_update_fuel_1(self):
        my_fuel: int = update_fuel(500, 8)
        self.assertEqual(492, my_fuel)

    def test_update_fuel_2(self):
        my_fuel: int = update_fuel(5, 0)
        self.assertEqual(5, my_fuel)

    def test_update_fuel_3(self):
        my_fuel: int = update_fuel(5, 9)
        self.assertEqual(0, my_fuel)

if __name__ == '__main__':
    unittest.main()
