
def check_valid(puzzle: list[list[int]], cages: list[list[int]]) -> bool:
    """This function returns False if the current puzzle board is invalid and True otherwise"""
    cages_valid: bool = check_cages_valid(puzzle, cages)
    columns_valid: bool = check_columns_valid(puzzle)
    rows_valid: bool = check_rows_valid(puzzle)
    return cages_valid and columns_valid and rows_valid

def check_cages_valid(puzzle: list[list[int]], cages: list[list[int]]) -> bool:
    """This function returns False if any of the cages are invalid and True otherwise."""
    for cage in cages:
        cage_cell_values: list[int] = get_cage_values(puzzle, cage)
        cage_is_full: bool = not (0 in cage_cell_values)
        if cage_is_full:
            if not full_cage_is_valid(puzzle, cage):
                return False
        else:
            if not partial_cage_is_valid(puzzle, cage):
                return False

    return True

def full_cage_is_valid(puzzle: list[list[int]], cage: list[int]) -> bool:
    if len(cage) < 3:
        raise ValueError(f'Cage: {cage} has not been defined properly!')
    cage_sum: int = cage[0]
    cage_cell_values: list[int] = get_cage_values(puzzle, cage)

    return sum(cage_cell_values) == cage_sum

def partial_cage_is_valid(puzzle: list[list[int]], cage: list[int]) -> bool:
    if len(cage) < 3:
        raise ValueError(f'Cage: {cage} has not been defined properly!')
    cage_sum: int = cage[0]
    cage_cell_values: list[int] = get_cage_values(puzzle, cage)

    return sum(cage_cell_values) < cage_sum

def get_cage_values(puzzle: list[list[int]], cage: list[int]) -> list[int]:
    """Takes in list of cage indices (0-24) and returns puzzle values at those indices"""
    N: int = len(puzzle)
    cage_values: list[int] = []
    cage_cell_inds = cage[2:]

    for global_ind in cage_cell_inds:
        row_ind: int = global_ind // N
        col_ind: int = global_ind % N
        cage_values.append(puzzle[row_ind][col_ind])

    return cage_values

def check_columns_valid(puzzle: list[list[int]]) -> bool:
    """This function returns False if duplicates exists in any column and True otherwise."""
    transposed_puzzle = get_puzzle_columns(puzzle)
    return check_rows_valid(transposed_puzzle)

def get_puzzle_columns(puzzle: list[list[int]]) -> list[list[int]]:
    """Transforms a puzzle from a list of rows instead a list of its columns"""
    row_length: int = len(puzzle[0])
    num_rows: int = len(puzzle)
    puzzle_columns: list[list[int]] = []

    for col_ind in range(row_length):
        col: list[int] = []
        for row_ind in range(num_rows):
            col.append(puzzle[row_ind][col_ind])
        puzzle_columns.append(col)

    return puzzle_columns

def check_rows_valid(puzzle: list[list[int]]) -> bool:
    """This function returns False if duplicates exists in any row and True otherwise."""
    for row in puzzle:
        row_without_zeros: list[int] = [num for num in row if num != 0]
        row_nonzero_entries_set: set[int] = set(row_without_zeros)
        if len(row_without_zeros) != len(row_nonzero_entries_set):
            return False

    return True
