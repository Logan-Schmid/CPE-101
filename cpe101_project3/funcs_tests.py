import unittest
from unittest.mock import patch
import io
from solver_funcs import check_rows_valid, check_valid, check_cages_valid, check_columns_valid
from solver_funcs import get_puzzle_columns, get_cage_values, partial_cage_is_valid, full_cage_is_valid
import solver

class MyTestCase(unittest.TestCase):
    @patch('builtins.input', side_effect=['9',
                                     '5 2 0 5',
                                     '8 3 1 2 6',
                                     '8 2 3 8',
                                     '6 3 4 9 14',
                                     '13 3 7 12 13',
                                     '5 2 10 15',
                                     '14 4 11 16 20 21',
                                     '6 3 17 18 22',
                                     '10 3 19 23 24'])
    def test_get_cages_1(self, mock_input):
        cages = solver.get_cages()
        solution: list[list[int]] = [[5, 2, 0, 5],
                                     [8, 3, 1, 2, 6],
                                     [8, 2, 3, 8],
                                     [6, 3, 4, 9, 14],
                                     [13, 3, 7, 12, 13],
                                     [5, 2, 10, 15],
                                     [14, 4, 11, 16, 20, 21],
                                     [6, 3, 17, 18, 22],
                                     [10, 3, 19, 23, 24]]
        self.assertListEqual(solution, cages)


    @patch('builtins.input', side_effect=['9',
                                     '5 2 0 5',
                                     '8 3 1 2 6',
                                     '8 2 3 8',
                                     '6 3 4 9 14',
                                     '13 3 7 12 13',
                                     '5 2 10 15',
                                     '14 4 11 16 20 21',
                                     '6 3 17 18 22',
                                     '10 3 19 23 24'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_1(self, mock_stdout, mock_input):
        solver.main()
        solution: str = """4 1 2 5 3
1 5 4 3 2
2 3 5 4 1
3 4 1 2 5
5 2 3 1 4"""
        solution_output_unittest: str = f"""--Solution--

{solution}

checks: 2265 backtracks: 438"""
        self.assertEqual(solution_output_unittest, mock_stdout.getvalue().strip())

    @patch('builtins.input', side_effect=['6',
                                          '11 4 0 5 10 15',
                                          '18 6 1 2 3 4 8 9',
                                          '33 10 6 7 11 12 13 16 18 21 23 24',
                                          '6 2 14 19',
                                          '3 2 17 22',
                                          '4 1 20'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_2(self, mock_stdout, mock_input):
        solver.main()
        solution: str = """1 3 4 2 5
2 4 5 3 1
5 2 3 1 4
3 5 1 4 2
4 1 2 5 3"""
        solution_output: str = f"""--Solution--

{solution}

checks: 3271 backtracks: 509"""
        self.assertEqual(solution_output, mock_stdout.getvalue().strip())

    def test_check_valid_1(self):
        puzzle = [[4, 1, 2, 5, 3],
                  [1, 5, 4, 3, 2],
                  [2, 3, 5, 4, 1],
                  [3, 4, 1, 2, 5],
                  [5, 2, 3, 1, 4]]

        cages = [[5, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]
        is_valid: bool = check_valid(puzzle, cages)
        self.assertTrue(is_valid)

    def test_check_valid_2(self):
        puzzle = [[4, 1, 2, 5, 3],
                  [1, 5, 4, 3, 2],
                  [2, 3, 5, 4, 1],
                  [3, 4, 1, 2, 5],
                  [5, 2, 3, 1, 4]]

        cages = [[2, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]
        is_valid: bool = check_valid(puzzle, cages)
        self.assertFalse(is_valid)

    def test_check_valid_3(self):
        puzzle = [[4, 1, 2, 5, 3],
                  [1, 5, 4, 3, 2],
                  [2, 3, 0, 4, 1],
                  [3, 4, 1, 2, 5],
                  [5, 2, 3, 1, 4]]

        cages = [[5, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]
        is_valid: bool = check_valid(puzzle, cages)
        self.assertTrue(is_valid)

    def test_check_valid_4(self):
        puzzle = [[4, 1, 2, 5, 3],
                  [1, 5, 4, 3, 2],
                  [2, 3, 3, 4, 1],
                  [3, 4, 1, 2, 5],
                  [5, 2, 3, 1, 4]]

        cages = [[5, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]
        is_valid: bool = check_valid(puzzle, cages)
        self.assertFalse(is_valid)

    def test_check_cages_valid_1(self):
        puzzle = [[4, 1, 2, 5, 3],
                  [1, 5, 4, 3, 2],
                  [2, 3, 5, 4, 1],
                  [3, 4, 1, 2, 5],
                  [5, 2, 3, 1, 4]]

        cages = [[5, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]
        is_valid: bool = check_cages_valid(puzzle, cages)
        self.assertTrue(is_valid)

    def test_check_cages_valid_2(self):
        puzzle = [[4, 1, 2, 5, 3],
                  [1, 5, 4, 3, 2],
                  [2, 3, 5, 4, 1],
                  [3, 4, 1, 0, 5],
                  [5, 2, 3, 1, 4]]

        cages = [[5, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]
        is_valid: bool = check_cages_valid(puzzle, cages)
        self.assertTrue(is_valid)

    def test_check_cages_valid_3(self):
        puzzle = [[4, 1, 2, 5, 3],
                  [1, 5, 4, 3, 2],
                  [2, 3, 5, 4, 1],
                  [3, 4, 1, 2, 5],
                  [5, 2, 3, 1, 5]]

        cages = [[5, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]
        is_valid: bool = check_cages_valid(puzzle, cages)
        self.assertFalse(is_valid)

    def test_check_cages_valid_4(self):
        puzzle = [[4, 1, 2, 5, 3],
                  [1, 0, 4, 3, 2],
                  [2, 3, 0, 4, 0],
                  [3, 4, 1, 2, 5],
                  [0, 0, 0, 0, 0]]

        cages = [[5, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]
        is_valid: bool = check_cages_valid(puzzle, cages)
        self.assertTrue(is_valid)

    def test_check_cages_valid_5(self):
        puzzle = [[4, 1, 2, 5, 3],
                  [1, 5, 4, 3, 2],
                  [2, 3, 5, 4, 1],
                  [3, 4, 1, 2, 5],
                  [5, 2, 3, 1, 4]]

        cages = [[75, 25] + list(range(25))]
        is_valid: bool = check_cages_valid(puzzle, cages)
        self.assertTrue(is_valid)

    def test_get_cage_values_1(self):
        puzzle = [[4, 1, 2, 5, 3],
                  [1, 5, 4, 3, 2],
                  [2, 3, 5, 4, 1],
                  [3, 4, 1, 2, 5],
                  [5, 2, 3, 1, 4]]

        cages = [   [5, 2, 0, 5],
                    [8, 3, 1, 2, 6],
                    [8, 2, 3, 8],
                    [6, 3, 4, 9, 14],
                    [13, 3, 7, 12, 13],
                    [5, 2, 10, 15],
                    [14, 4, 11, 16, 20, 21],
                    [6, 3, 17, 18, 22],
                    [10, 3, 19, 23, 24]]
        my_cage = cages[0]
        cage_values = get_cage_values(puzzle, my_cage)
        solution = [4, 1]
        self.assertListEqual(solution, cage_values)

    def test_get_cage_values_2(self):
        puzzle = [[4, 1, 2, 5, 3],
                  [1, 5, 4, 3, 2],
                  [2, 3, 5, 4, 1],
                  [3, 4, 1, 2, 5],
                  [5, 2, 3, 1, 4]]

        cages = [   [5, 2, 0, 5],
                    [8, 3, 1, 2, 6],
                    [8, 2, 3, 8],
                    [6, 3, 4, 9, 14],
                    [13, 3, 7, 12, 13],
                    [5, 2, 10, 15],
                    [14, 4, 11, 16, 20, 21],
                    [6, 3, 17, 18, 22],
                    [10, 3, 19, 23, 24]]
        my_cage = cages[6]
        cage_values = get_cage_values(puzzle, my_cage)
        solution = [3, 4, 5, 2]
        self.assertListEqual(solution, cage_values)

    def test_check_rows_valid_1(self):
        puzzle = [[1, 1, 1, 1, 1],
                  [0, 2, 0, 0, 0],
                  [3, 3, 3, 3, 3],
                  [0, 0, 0, 4, 0],
                  [5, 5, 5, 5, 5]]
        is_valid: bool = check_rows_valid(puzzle)
        self.assertFalse(is_valid)

    def test_check_rows_valid_2(self):
        puzzle = [[1, 0, 0, 0, 0],
                  [0, 2, 0, 0, 0],
                  [0, 0, 3, 0, 0],
                  [0, 0, 0, 4, 0],
                  [0, 0, 0, 0, 5]]
        is_valid: bool = check_rows_valid(puzzle)
        self.assertTrue(is_valid)

    def test_check_rows_valid_3(self):
        puzzle = [[1, 2, 3, 4, 5],
                  [2, 3, 4, 5, 1],
                  [3, 4, 5, 1, 2],
                  [4, 5, 1, 2, 3],
                  [5, 1, 2, 3, 4]]
        is_valid: bool = check_rows_valid(puzzle)
        self.assertTrue(is_valid)

    def test_check_rows_valid_4(self):
        puzzle = [[1, 2, 3, 4, 5],
                  [2, 0, 4, 5, 1],
                  [3, 4, 5, 1, 2],
                  [4, 5, 1, 2, 3],
                  [5, 1, 2, 3, 0]]
        is_valid: bool = check_rows_valid(puzzle)
        self.assertTrue(is_valid)

    def test_check_rows_valid_5(self):
        puzzle = [[1, 2, 3, 4, 5],
                  [2, 3, 4, 5, 2],
                  [3, 4, 5, 1, 2],
                  [4, 5, 1, 2, 3],
                  [5, 0, 2, 3, 4]]
        is_valid: bool = check_rows_valid(puzzle)
        self.assertFalse(is_valid)

    def test_check_column_valid_1(self):
        puzzle = [[1, 2, 3, 4, 5],
                  [2, 3, 4, 5, 1],
                  [3, 4, 5, 1, 2],
                  [4, 5, 1, 2, 3],
                  [5, 1, 2, 3, 4]]
        is_valid: bool = check_columns_valid(puzzle)
        self.assertTrue(is_valid)

    def test_check_column_valid_2(self):
        puzzle = [[1, 2, 3, 4, 5],
                  [2, 0, 4, 5, 1],
                  [3, 4, 5, 1, 2],
                  [4, 5, 1, 2, 3],
                  [5, 1, 2, 3, 0]]
        is_valid: bool = check_columns_valid(puzzle)
        self.assertTrue(is_valid)

    def test_check_column_valid_3(self):
        puzzle = [[1, 2, 3, 4, 5],
                  [2, 3, 4, 5, 2],
                  [3, 4, 5, 1, 2],
                  [4, 5, 1, 2, 3],
                  [1, 1, 2, 3, 0]]
        is_valid: bool = check_columns_valid(puzzle)
        self.assertFalse(is_valid)

    def test_check_column_valid_4(self):
        puzzle = [[1, 1, 1, 1, 1],
                  [0, 2, 0, 0, 0],
                  [3, 3, 3, 3, 3],
                  [0, 0, 0, 4, 0],
                  [5, 5, 5, 5, 5]]
        is_valid: bool = check_columns_valid(puzzle)
        self.assertTrue(is_valid)

    def test_get_puzzle_columns_1(self):
        puzzle = [[1, 1, 1, 1, 1],
                  [0, 2, 0, 0, 0],
                  [3, 3, 3, 3, 3],
                  [0, 0, 0, 4, 0],
                  [5, 5, 5, 5, 5]]

        correct = [[1, 0, 3, 0, 5],
                   [1, 2, 3, 0, 5],
                   [1, 0, 3, 0, 5],
                   [1, 0, 3, 4, 5],
                   [1, 0, 3, 0, 5]]
        puzzle_t = get_puzzle_columns(puzzle)
        self.assertListEqual(correct, puzzle_t)

    def test_get_puzzle_columns_2(self):
        puzzle = [[1, 0, 0, 0, 0],
                  [0, 2, 0, 0, 0],
                  [0, 0, 3, 0, 0],
                  [0, 0, 0, 4, 0],
                  [0, 0, 0, 0, 5]]

        correct = [[1, 0, 0, 0, 0],
                   [0, 2, 0, 0, 0],
                   [0, 0, 3, 0, 0],
                   [0, 0, 0, 4, 0],
                   [0, 0, 0, 0, 5]]
        puzzle_t = get_puzzle_columns(puzzle)
        self.assertListEqual(correct, puzzle_t)


if __name__ == '__main__':
    unittest.main()
