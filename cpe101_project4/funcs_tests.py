import unittest
from finder_funcs import *

class MyTestCase(unittest.TestCase):
    def test_WordInfo_eq_1(self):
        word_1: WordInfo = WordInfo('type', -1, -1, '')
        word_2: WordInfo = WordInfo('type', 0, -1, '')
        word_2.row = -1
        self.assertEqual(word_1, word_2)

    def test_WordInfo_eq_2(self):
        word_1: WordInfo = WordInfo('type', 5, 9, 'DOWN')
        word_2: WordInfo = WordInfo('type', 5, 0, 'DOWN')
        word_2.col = 9
        self.assertEqual(word_1, word_2)

    def test_WordInfo_eq_3(self):
        word_1: WordInfo = WordInfo('typo', 5, 9, 'DOWN')
        word_2: WordInfo = WordInfo('type', 5, 9, 'DOWN')
        self.assertNotEqual(word_1, word_2)

    def test_WordInfo_eq_4(self):
        word_1: WordInfo = WordInfo('type', 5, 9, 'UP')
        word_2: WordInfo = WordInfo('type', 5, 9, 'DOWN')
        self.assertNotEqual(word_1, word_2)

    def test_WordInfo_eq_5(self):
        word_1: WordInfo = WordInfo('type', 1, 9, 'DOWN')
        word_2: WordInfo = WordInfo('type', 5, 9, 'DOWN')
        self.assertNotEqual(word_1, word_2)

    def test_WordInfo_eq_6(self):
        word_1: WordInfo = WordInfo('type', 5, -1, 'DOWN')
        word_2: WordInfo = WordInfo('type', 5, 9, 'DOWN')
        self.assertNotEqual(word_1, word_2)


    def test_import_puzzle_1(self):
        puzzle_raw_text: str = """WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU
    UNIX CALPOLY GCC SLO CPE compile VIm test
    """
        puzzle_grid, words = import_puzzle(puzzle_raw_text)
        self.assertEqual(["WAQHGTTWEE", "CBMIVQQELS", "APXWKWIIIL", "LDELFXPIPV", "PONDTMVAMN", "OEDSOYQGOB", "LGQCKGMMCT", "YCSLOACUZM", "XVDMGSXCYZ", "UUIUNIXFNU"], puzzle_grid)
        self.assertEqual(['UNIX', 'CALPOLY', 'GCC', 'SLO', 'CPE', 'COMPILE', 'VIM', 'TEST'], words)

    def test_import_puzzle_2(self):
        puzzle_raw_text: str = """ABCDE
        AB  DE   CE 
        """
        puzzle_grid, words = import_puzzle(puzzle_raw_text)
        self.assertEqual(["ABCDE"], puzzle_grid)
        self.assertEqual(['AB', 'DE', 'CE'], words)

    def test_import_puzzle_3(self):
        puzzle_raw_text: str = """ABCDEFGHIJKLMNOP"""
        puzzle_grid, words = import_puzzle(puzzle_raw_text)
        self.assertEqual(["ABCDEFGHIJ", "KLMNOP"], puzzle_grid)
        self.assertEqual([], words)


    def test_search_word_right_1(self):
        puzzle_grid, words = import_puzzle('ABCDE')
        puzzle: Puzzle = Puzzle(puzzle_grid, words)
        result_word_info: WordInfo = search_word_right(puzzle, 'BC')
        self.assertEqual(WordInfo('BC', 0, 1, 'FORWARD'), result_word_info)  # add assertion here

    def test_search_word_right_2(self):
        puzzle_grid, words = import_puzzle("""aBCDEFGHIJkLMNOPQRSTuVWXYZAAAAvIMKKKKKKKKKKKKKK
        vim wayz AAAA""")
        puzzle: Puzzle = Puzzle(puzzle_grid, words)
        result_word_info: WordInfo = search_word_right(puzzle, puzzle.words[2])
        self.assertEqual(WordInfo('AAAA', 2, 6, 'FORWARD'), result_word_info)  # add assertion here

    def test_search_word_right_3(self):
        puzzle_grid, words = import_puzzle('ABCDEFGHIJKLMNOPEGGRWRFBIME')
        puzzle: Puzzle = Puzzle(puzzle_grid, words)
        result_word_info: WordInfo = search_word_right(puzzle, 'NOTINIT')
        self.assertEqual(WordInfo('NOTINIT', -1, -1, ''), result_word_info)

    def test_search_word_right_4(self):
        puzzle_grid, words = import_puzzle('ABCDEFGHIJKLMNOPEGGRWRFBIME')
        puzzle: Puzzle = Puzzle(puzzle_grid, words)
        result_word_info: WordInfo = search_word_right(puzzle, 'TOOLONGFORPUZZLE')
        self.assertEqual(WordInfo('TOOLONGFORPUZZLE', -1, -1, ''), result_word_info)

    def test_search_word_right_5(self):
        puzzle_grid, words = import_puzzle('')
        puzzle: Puzzle = Puzzle(puzzle_grid, words)
        result_word_info: WordInfo = search_word_right(puzzle, 'NOTINIT')
        self.assertEqual(WordInfo('NOTINIT', -1, -1, ''), result_word_info)

    def test_search_word_right_6(self):
        puzzle_grid, words = import_puzzle('ABCDEFGHIJKLMNOPEGGRWRFBIME')
        puzzle: Puzzle = Puzzle(puzzle_grid, words)
        result_word_info: WordInfo = search_word_right(puzzle, 'ONETOOLONGX')
        self.assertEqual(WordInfo('ONETOOLONGX', -1, -1, ''), result_word_info)


    def test_search_word_left_1(self):
        puzzle_grid, words = import_puzzle('ABCDEFGHIJKLMNOPEGGRWRFBIME')
        puzzle: Puzzle = Puzzle(puzzle_grid, words)
        result_word_info: WordInfo = search_word_left(puzzle, 'ONETOOLONGX')
        self.assertEqual(WordInfo('ONETOOLONGX', -1, -1, ''), result_word_info)

    def test_search_word_left_2(self):
        puzzle_grid, words = import_puzzle('ABMIVFGHIJKLMNOPEGGRWRFBIME')
        puzzle: Puzzle = Puzzle(puzzle_grid, words)
        result_word_info: WordInfo = search_word_left(puzzle, 'VIM')
        self.assertEqual(WordInfo('VIM', 0, 4, 'BACKWARD'), result_word_info)

    def test_search_word_left_3(self):
        puzzle_grid, words = import_puzzle('ABMIVFGHIJKLMNOPEGGRWRFBIME')
        puzzle: Puzzle = Puzzle(puzzle_grid, words)
        result_word_info: WordInfo = search_word_left(puzzle, 'VIM')
        self.assertEqual(WordInfo('VIM', 0, 4, 'BACKWARD'), result_word_info)

    def test_search_word_left_4(self):
        puzzle_grid, words = import_puzzle('ABMIVFGHIJkLMNOPEGGRwReMiHC')
        puzzle: Puzzle = Puzzle(puzzle_grid, words)
        result_word_info: WordInfo = search_word_left(puzzle, 'CHIME')
        self.assertEqual(WordInfo('CHIME', 2, 6, 'BACKWARD'), result_word_info)


    def test_search_word_down_1(self):
        puzzle_grid, words = import_puzzle('ABCDE')
        puzzle: Puzzle = Puzzle(puzzle_grid, words)
        result_word_info: WordInfo = search_word_down(puzzle, 'CHIME')
        self.assertEqual(WordInfo('CHIME', -1, -1, ''), result_word_info)

    def test_search_word_down_2(self):
        puzzle_grid, words = import_puzzle("""aBCRXXXXXXaKKIXXXXXXaWWGXXXXXXaRRHXXXXXXaPPTXXXXXX
        right""")
        puzzle: Puzzle = Puzzle(puzzle_grid, words)
        result_word_info: WordInfo = search_word_down(puzzle, 'RIGHT')
        self.assertEqual(WordInfo('RIGHT', 0, 3, 'DOWN'), result_word_info)

    def test_search_word_down_3(self):
        puzzle_grid, words = import_puzzle("""aBCRXXXXXXaKKIXXXXXXaWWGXXXXXXaRRHXXXXXXaPPT
        right""")
        puzzle: Puzzle = Puzzle(puzzle_grid, words)
        result_word_info: WordInfo = search_word_down(puzzle, 'IGHT')
        self.assertEqual(WordInfo('IGHT', 1, 3, 'DOWN'), result_word_info)

    def test_search_word_down_4(self):
        puzzle_grid, words = import_puzzle("""aBCRXXXXXPaKKIXXXXXAaWWGXXXXXSaRRHXXXXXSaPPTXXXXX
        Pass""")
        puzzle: Puzzle = Puzzle(puzzle_grid, words)
        result_word_info: WordInfo = search_word_down(puzzle, 'PASS')
        self.assertEqual(WordInfo('PASS', 0, 9, 'DOWN'), result_word_info)


    def test_search_word_up_1(self):
        puzzle_grid, words = import_puzzle('ABCDE')
        puzzle: Puzzle = Puzzle(puzzle_grid, words)
        result_word_info: WordInfo = search_word_up(puzzle, 'CHIME')
        self.assertEqual(WordInfo('CHIME', -1, -1, ''), result_word_info)

    def test_search_word_up_2(self):
        puzzle_grid, words = import_puzzle("""aBCTXXXXXXaKKHXXXXXXaWWGXXXXXXaRRIXXXXXXaPPRXXXXXX
        Right""")
        puzzle: Puzzle = Puzzle(puzzle_grid, words)
        result_word_info: WordInfo = search_word_up(puzzle, 'RIGHT')
        self.assertEqual(WordInfo('RIGHT', 4, 3, 'UP').__dict__, result_word_info.__dict__)

    def test_search_word_up_3(self):
        puzzle_grid, words = import_puzzle("""aBCRXXXXXSaKKIXXXXXSaWWGXXXXXAaRRHXXXXXPaPPTXXXXX
        Pass""")
        puzzle: Puzzle = Puzzle(puzzle_grid, words)
        result_word_info: WordInfo = search_word_up(puzzle, 'PASS')
        self.assertEqual(WordInfo('PASS', 3, 9, 'UP'), result_word_info)


    def test_search_word_diagonal_1(self):
        puzzle_grid, words = import_puzzle("""aBCRXXXXXSaKEIXXXXXSaWWEXXXXXAaRRHXXXXXPaPPTXXXXX
        BEE""")
        puzzle: Puzzle = Puzzle(puzzle_grid, words)
        result_word_info: WordInfo = search_word_diagonal(puzzle, 'BEE')
        self.assertEqual(WordInfo('BEE', 0, 1, 'DIAGONAL'), result_word_info)

    def test_search_word_diagonal_2(self):
        puzzle_grid, words = import_puzzle("aBCRXXXXXXaDFG")
        puzzle: Puzzle = Puzzle(puzzle_grid, words)
        result_word_info: WordInfo = search_word_diagonal(puzzle, 'SH')
        self.assertEqual(WordInfo('SH', -1, -1, ''), result_word_info)

    def test_search_word_diagonal_3(self):
        puzzle_grid, words = import_puzzle("""JFFMGHTSKPETRULMJCDHVEIMNLWYZLISHPFCFNNHGTBYLWTSWEDEMJAAAILLCREVGZDTOPUADNYFEJCNMHZFMELJVHBPGETXKVNL
        tester function help flag watch bmed alakazam""")
        puzzle: Puzzle = Puzzle(puzzle_grid, words)
        result_word_info: WordInfo = search_word_diagonal(puzzle, 'WATCH')
        self.assertEqual(WordInfo('WATCH', 4, 5, 'DIAGONAL'), result_word_info)

    def test_find_word_1(self):
        puzzle_grid, words = import_puzzle("""JFFMGHTSKPETRULMJCDHVEIMNLWYZLISHPFCFNNHGTBYLWTSWEDEMJAAAILLCREVGZDTOPUADNYFEJCNMHZFMELJVHBPGETXKVNL
                tester function help flag watch bmed alakazam""")
        puzzle: Puzzle = Puzzle(puzzle_grid, words)
        result_word_info: WordInfo = find_word(puzzle, 'Watch')
        self.assertEqual(WordInfo('WATCH', 4, 5, 'DIAGONAL'), result_word_info)


if __name__ == '__main__':
    unittest.main()
