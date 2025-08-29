import unittest
from unittest.mock import patch
import io
from lander_funcs import *


class TestIOFuncs(unittest.TestCase):
    # @patch('builtins.input', return_value='')  # mock input
    @patch('sys.stdout', new_callable=io.StringIO)  # capture output
    def test_something_show_welcome(self, mock_stout):
        show_welcome()
        self.assertEqual(mock_stout.getvalue().strip(),
                         """-----------------------------------------------------------------
--------- Welcome to the moon lander simulation program ---------
-----------------------------------------------------------------""")


    @patch('builtins.input', return_value='1300')
    def test_get_altitude_1(self, mock_input):
        my_altitude: int = get_altitude()
        self.assertEqual(my_altitude, 1300)

    @patch('builtins.input', side_effect=['10000', '1000'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_altitude_2(self, mock_stdout, mock_input):
        my_altitude: int = get_altitude()
        self.assertEqual(my_altitude, 1000)
        self.assertEqual(mock_stdout.getvalue().strip(), 'Error: Input must be between 1 and 9999!')

    @patch('builtins.input', side_effect=['-1', '0', '1000'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_altitude_4(self, mock_stdout, mock_input):
        my_altitude: int = get_altitude()
        self.assertEqual(my_altitude, 1000)
        self.assertEqual(mock_stdout.getvalue().strip(), 'Error: Input must be between 1 and 9999!\nError: Input must be between 1 and 9999!')

    @patch('builtins.input', side_effect=['a', '500'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_altitude_5(self, mock_stdout, mock_input):
        my_altitude: int = get_altitude()
        self.assertEqual(my_altitude, 500)
        self.assertEqual(mock_stdout.getvalue().strip(), 'Error: Input must be an integer!')


    @patch('builtins.input', return_value='200')
    def test_get_fuel_1(self, mock_input):
        my_fuel: int = get_fuel()
        self.assertEqual(my_fuel, 200)

    @patch('builtins.input', side_effect=['0', '100'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_fuel_2(self, mock_stdout, mock_input):
        my_fuel: int = get_fuel()
        self.assertEqual(my_fuel, 100)
        self.assertTrue('Error: input must be greater than 0!' in mock_stdout.getvalue().strip())

    @patch('builtins.input', side_effect=['-10', '100'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_fuel_3(self, mock_stdout, mock_input):
        my_fuel: int = get_fuel()
        self.assertEqual(my_fuel, 100)
        self.assertTrue('Error: input must be greater than 0!' in mock_stdout.getvalue().strip())

    @patch('builtins.input', side_effect=['-_', '100'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_fuel_4(self, mock_stdout, mock_input):
        my_fuel: int = get_fuel()
        self.assertEqual(my_fuel, 100)
        self.assertTrue('Error: must input an integer!' in mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_lm_state(self, mock_stdout):
        display_lm_state(20, 1000, 35, 400, 40)
        correct_output: str = """The current state of the lunar module is:
    Elapsed Time: 20 seconds
    Altitude: 1000 meters
    Velocity: 35 m/s
    Fuel Remaining: 400 Liters
    Rate of Fuel Consumption: 40 L/s"""
        self.assertTrue(correct_output in mock_stdout.getvalue().strip())


    @patch('builtins.input', return_value='0')
    def test_get_fuel_rate_1(self, mock_input):
        my_fuel_rate: int = get_fuel_rate(400)
        self.assertEqual(my_fuel_rate, 0)

    @patch('builtins.input', side_effect=['-1', '1.5', 'a', '10', '9'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_fuel_rate_2(self, mock_stdout, mock_input):
        my_fuel_rate: int = get_fuel_rate(400)
        self.assertEqual(9, my_fuel_rate)
        error_text: str = "Error: input must be between 0-9, inclusive!\nError: input must be an integer!\nError: input must be an integer!\nError: input must be between 0-9, inclusive!"
        self.assertTrue(error_text in mock_stdout.getvalue().strip())

    @patch('builtins.input', return_value='8')
    def test_get_fuel_rate_3(self, mock_input):
        my_fuel_rate: int = get_fuel_rate(5)
        self.assertEqual(my_fuel_rate, 5)


    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_lm_landing_status_1(self, mock_stdout):
        display_lm_landing_status(0)
        correct_message: str = 'Status at landing - The eagle has landed!'
        self.assertTrue(correct_message in mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_lm_landing_status_2(self, mock_stdout):
        display_lm_landing_status(-1)
        correct_message: str = 'Status at landing - The eagle has landed!'
        self.assertTrue(correct_message in mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_lm_landing_status_3(self, mock_stdout):
        display_lm_landing_status(-4.9)
        correct_message: str = 'Status at landing - Enjoy your oxygen while it lasts!'
        self.assertTrue(correct_message in mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_lm_landing_status_4(self, mock_stdout):
        display_lm_landing_status(-10)
        correct_message: str = 'Status at landing - Ouch - that hurt!'
        self.assertTrue(correct_message in mock_stdout.getvalue().strip())

if __name__ == '__main__':
    unittest.main()
