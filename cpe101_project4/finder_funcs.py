from typing import Self

class Puzzle:
    def __init__(self, puzzle_grid: list[str], words: list[str]):
        self.puzzle_grid = puzzle_grid
        self.words = words

    def __str__(self):
        formatted_puzzle: str = ''
        for row in self.puzzle_grid:
            formatted_puzzle += row.rstrip() + '\n'

        return formatted_puzzle + f'\nSearching for words: {self.words}'

class WordInfo:
    def __init__(self, word: str, row: int, col: int, direction: str):
        self.word = word
        self.row = row
        self.col = col
        self.direction = direction

    def __eq__(self, other: Self) -> bool:
        return self.__dict__ == other.__dict__

def import_puzzle(puzzle_raw_text) -> (list[str], list[str]):
    puzzle_formatted: list[str] = puzzle_raw_text.split('\n')
    puzzle_line: str = puzzle_formatted[0].strip().upper()

    puzzle_grid: list[str] = []
    while len(puzzle_line) >= 10:
        puzzle_grid.append(puzzle_line[:10])
        puzzle_line = puzzle_line[10:]
    if puzzle_line:
        puzzle_grid.append(puzzle_line)

    # check if no words to check were given
    if len(puzzle_formatted) <= 1 or not puzzle_formatted[1].strip():
        return puzzle_grid, []

    words_line: str = puzzle_formatted[1].strip().upper()
    words: list[str] = words_line.split(' ')
    words = [word.strip() for word in words if word]
    return puzzle_grid, words

def remove_spaces_from_puzzle(file_name: str) -> None:
    with open(file_name, 'r+') as file:
        lines: list[str] = file.readlines()
        new_text: list[str] = []
        for line in lines:
            updated_line: str = line.replace(' ', '')
            new_text.append(updated_line)

        file.seek(0)
        file.truncate()
        file.writelines(new_text)

def find_word(puzzle: Puzzle, word: str) -> WordInfo:
    """
    Returns a Word with its location details within the puzzle.
    Assigns row=col=-1, direction='' if the word cannot be found.
    :param word: Word to be searched for
    :param puzzle: Puzzle to be searched within
    :return: Word object with location details
    """
    word = word.upper()

    word_location: WordInfo = search_word_right(puzzle, word)
    if word_location.direction:
        return word_location

    word_location: WordInfo = search_word_left(puzzle, word)
    if word_location.direction:
        return word_location

    word_location: WordInfo = search_word_down(puzzle, word)
    if word_location.direction:
        return word_location

    word_location: WordInfo = search_word_up(puzzle, word)
    if word_location.direction:
        return word_location

    word_location: WordInfo = search_word_diagonal(puzzle, word)

    return word_location

def search_word_right(puzzle: Puzzle, word: str):
    grid = puzzle.puzzle_grid
    word_length: int = len(word)

    for row_ind, line in enumerate(grid):
        line_length: int = len(line)

        for col_ind in range(line_length - word_length + 1):
            if line[col_ind : col_ind+word_length] == word:
                return WordInfo(word, row_ind, col_ind, 'FORWARD')

    return WordInfo(word, -1, -1, '')

def search_word_left(puzzle: Puzzle, word: str):
    grid = puzzle.puzzle_grid
    word_length: int = len(word)

    for row_ind, line in enumerate(grid):
        line_length: int = len(line)
        line = line[::-1]
        for col_ind in range(line_length - word_length + 1):
            if line[col_ind : col_ind+word_length] == word:
                col_ind = (line_length -1) - col_ind
                return WordInfo(word, row_ind, col_ind, 'BACKWARD')

    return WordInfo(word, -1, -1, '')

def search_word_down(puzzle: Puzzle, word: str):
    grid = puzzle.puzzle_grid
    word_length: int = len(word)
    num_rows: int = len(grid)
    num_cols: int = len(grid[0])
    last_line_length: int = len(grid[-1])

    for col in range(num_cols):
        # make the column string to check for word
        transposed_line: str = ''.join([grid[row][col] for row in range(num_rows - 1)])
        if col < last_line_length:
            transposed_line += grid[num_rows-1][col]

        # now check the column string for word, no need to store it
        for row_ind in range(len(transposed_line) - word_length + 1):
            if transposed_line[row_ind : row_ind + word_length] == word:
                return WordInfo(word, row_ind, col, 'DOWN')

    return WordInfo(word, -1, -1, '')

def search_word_up(puzzle: Puzzle, word: str):
    grid = puzzle.puzzle_grid
    word_length: int = len(word)
    num_rows: int = len(grid)
    num_cols: int = len(grid[0])
    last_line_length: int = len(grid[-1])

    for col in range(num_cols):
        # make the column string to check for word
        transposed_line: str = ''.join([grid[row][col] for row in range(num_rows - 1)])
        if col < last_line_length:
            transposed_line += grid[num_rows - 1][col]

        transposed_line = transposed_line[::-1]
        # now check the column string for word, no need to store it
        for row_ind in range(len(transposed_line) - word_length + 1):
            if transposed_line[row_ind: row_ind + word_length] == word:
                return WordInfo(word, (len(transposed_line) - row_ind - 1), col, 'UP')

    return WordInfo(word, -1, -1, '')

def search_word_diagonal(puzzle: Puzzle, word: str):
    """
    Searches along the down-right diagonal only
    :return: WordInfo of the starting char of word found puzzle
    """
    grid: list[str] = puzzle.puzzle_grid
    num_rows: int = len(grid)
    num_cols: int = len(grid[0])
    num_diagonals: int = num_rows + num_cols - 1
    last_line_len: int = len(grid[-1])

    for diag_ind in range(num_diagonals):
        if diag_ind < num_cols:
            row: int = 0
            col: int = num_cols - diag_ind - 1
        else:
            row: int = diag_ind - num_cols + 1
            col: int = 0
        start_row: int = row
        start_col: int = col

        # get diagonal string
        diag_line: str = ''
        while row < num_rows and col < num_cols:
            if row == (num_rows - 1) and col >= last_line_len:
                break
            diag_line += grid[row][col]
            row += 1; col += 1

        for i in range(len(diag_line) - len(word) + 1):
            if diag_line[i : i + len(word)] == word:
                return WordInfo(word, start_row + i, start_col + i, 'DIAGONAL')

    return WordInfo(word, -1, -1, '')

def solve_puzzle(puzzle: Puzzle) -> list[WordInfo]:
    word_locations: list[WordInfo] = []
    for word in puzzle.words:
        word_locations.append(find_word(puzzle, word))

    return word_locations

def display_formatted_solution(word_locations: list[WordInfo]) -> None:
    for word_info in word_locations:
        if word_info.row != -1:
            print(f'{word_info.word.upper()}: ({word_info.direction.upper()}) row: {word_info.row} column: {word_info.col}')
        else:
            print(f'{word_info.word}: word not found')
