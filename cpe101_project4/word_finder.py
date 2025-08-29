import sys
from finder_funcs import *

def main():
    puzzle_raw_text: str = sys.stdin.read()
    puzzle_grid, words = import_puzzle(puzzle_raw_text)
    puzzle: Puzzle = Puzzle(puzzle_grid, words)
    print(puzzle)

    word_info: list[WordInfo] = solve_puzzle(puzzle)
    display_formatted_solution(word_info)

if __name__ == '__main__':
    main()

