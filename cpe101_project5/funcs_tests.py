import unittest
from quake_funcs import Earthquake, read_quakes_from_file, output_quakes, filter_by_mag, filter_by_place
from unittest.mock import patch
import io
from datetime import datetime

class MyTestCase(unittest.TestCase):
    def test_Earthquake_eq_1(self):
        quake1: Earthquake = Earthquake('Here', 7.3, 132.111, -14.1234, 10)
        quake2: Earthquake = Earthquake('There', 7.3, 132.111, -14.1234, 10)
        self.assertNotEqual(quake1, quake2)

    def test_Earthquake_eq_2(self):
        quake1: Earthquake = Earthquake('Here', 7.3, 132.111, -14.1234, 10)
        quake2: Earthquake = Earthquake('There', 7.3, 132.111, -14.1234, 10)
        quake2.place = 'Here'
        self.assertEqual(quake1, quake2)

    def test_read_quakes_from_file_1(self):
        with open('quakes0.txt') as file:
            result_quakes: list[Earthquake] = read_quakes_from_file(file)
        actual: list[Earthquake] = [Earthquake("9km E of Running Springs, CA",1.05, -117.0085, 34.2036667, 1488185465),
                                    Earthquake("5km S of Gilroy, California",2.19, -121.5801697, 36.9580002, 1488173538)]
        self.assertListEqual(actual, result_quakes)

    def test_read_quakes_from_file_2(self):
        with open('quakes1.txt') as file:
            result_quakes: list[Earthquake] = read_quakes_from_file(file)
        actual: list[Earthquake] = [Earthquake("HERE!!!",3.91, -117.0085, -34.2036667, 1488185465),
                                    Earthquake("-5 miles from the border of my town",-1.21, 121.5801697, 0, 3)]
        self.assertListEqual(actual, result_quakes)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_output_quakes_1(self, mock_stdout):
        with open('quakes0.txt') as file:
            result_quakes: list[Earthquake] = read_quakes_from_file(file)
        output_quakes(result_quakes)
        output_text: str = mock_stdout.getvalue().strip()
        self.assertEqual(f"""Earthquakes:\n------------
(1.05){12*' '}9km E of Running Springs, CA at {datetime.fromtimestamp(1488185465)} (-117.008, 34.204)
(2.19){13*' '}5km S of Gilroy, California at {datetime.fromtimestamp(1488173538)} (-121.580, 36.958)""",
                         output_text)

    def test_filter_by_mag_1(self):
        with open('quakes0.txt') as file:
            result_quakes: list[Earthquake] = read_quakes_from_file(file)
        filtered_quakes = filter_by_mag(result_quakes, 1, 2.19)
        actual: list[Earthquake] = [Earthquake("9km E of Running Springs, CA", 1.05, -117.0085, 34.2036667, 1488185465),
                                    Earthquake("5km S of Gilroy, California", 2.19, -121.5801697, 36.9580002,1488173538)]
        self.assertListEqual(actual, filtered_quakes)

    def test_filter_by_mag_2(self):
        with open('quakes0.txt') as file:
            result_quakes: list[Earthquake] = read_quakes_from_file(file)
        filtered_quakes = filter_by_mag(result_quakes, 1.5, 2.5)
        actual: list[Earthquake] = [Earthquake("5km S of Gilroy, California", 2.19, -121.5801697, 36.9580002,1488173538)]
        self.assertListEqual(actual, filtered_quakes)

    def test_filter_by_mag_3(self):
        with open('quakes0.txt') as file:
            result_quakes: list[Earthquake] = read_quakes_from_file(file)
        filtered_quakes = filter_by_mag(result_quakes, 1, 2)
        actual: list[Earthquake] = [Earthquake("9km E of Running Springs, CA", 1.05, -117.0085, 34.2036667, 1488185465)]
        self.assertListEqual(actual, filtered_quakes)


    def test_filter_by_place_1(self):
        with open('quakes0.txt') as file:
            result_quakes: list[Earthquake] = read_quakes_from_file(file)
        filtered_quakes = filter_by_place(result_quakes, 'km')
        actual: list[Earthquake] = [Earthquake("9km E of Running Springs, CA", 1.05, -117.0085, 34.2036667, 1488185465),
                                    Earthquake("5km S of Gilroy, California", 2.19, -121.5801697, 36.9580002,1488173538)]
        self.assertListEqual(actual, filtered_quakes)

    def test_filter_by_place_2(self):
        with open('quakes0.txt') as file:
            result_quakes: list[Earthquake] = read_quakes_from_file(file)
        filtered_quakes = filter_by_place(result_quakes, 'Running')
        actual: list[Earthquake] = [Earthquake("9km E of Running Springs, CA", 1.05, -117.0085, 34.2036667, 1488185465)]
        self.assertListEqual(actual, filtered_quakes)

    def test_filter_by_place_3(self):
        with open('quakes0.txt') as file:
            result_quakes: list[Earthquake] = read_quakes_from_file(file)
        filtered_quakes = filter_by_place(result_quakes, 'S of Gilroy')
        actual: list[Earthquake] = [Earthquake("5km S of Gilroy, California", 2.19, -121.5801697, 36.9580002,1488173538)]
        self.assertListEqual(actual, filtered_quakes)

    def test_filter_by_place_4(self):
        with open('quakes0.txt') as file:
            result_quakes: list[Earthquake] = read_quakes_from_file(file)
        filtered_quakes = filter_by_place(result_quakes, 'ca')
        actual: list[Earthquake] = [Earthquake("9km E of Running Springs, CA", 1.05, -117.0085, 34.2036667, 1488185465),
                                    Earthquake("5km S of Gilroy, California", 2.19, -121.5801697, 36.9580002, 1488173538)]
        self.assertListEqual(actual, filtered_quakes)

if __name__ == '__main__':
    unittest.main()
