from solver_funcs import check_valid

def get_cages() -> list[list[int]]:
    """
    Prompts the user for a number of cages and will then prompt the user for that many cages.
    Assumes all input will be valid.
    """
    while True:
        num_cages = int(input('Number of cages: ').strip())
        try:
            if 0 <= num_cages <= 25:
                break
            else:
                print('Error: Number of cages must be between 1-25!')
        except ValueError:
            print('Error: must input an integer value!')

    cages: list[list[int]] = []
    for i in range(num_cages):
        cage: list[int] = [int(entry) for entry in input(f"Cage number {i}: ").strip().split(' ')]
        cages.append(cage)

    return cages

def main():
    N: int = 5
    puzzle: list[list[int]] = [N*[0] for i in range(N)]
    cages: list[list[int]] = get_cages()
    num_checks: int = 0
    num_backtracks: int = 0

    current_row: int = 0
    current_col: int = 0
    puzzle_is_unsolvable: bool = False

    while (current_row < N) and (not puzzle_is_unsolvable):
        backtrack_flag: bool = False
        puzzle[current_row][current_col] += 1
        if puzzle[0][0] == 6:
            puzzle_is_unsolvable = True

        num_checks += 1
        while not check_valid(puzzle, cages):
            if puzzle[current_row][current_col] > N:
                backtrack_flag = True
                puzzle[current_row][current_col] = 0
                break
            puzzle[current_row][current_col] += 1
            num_checks += 1

        if backtrack_flag:
            num_backtracks += 1
            if current_col == 0:
                current_row -= 1
                current_col = 4
            else:
                current_col -= 1
        else:
            if current_col == 4:
                current_row += 1
                current_col = 0
            else:
                current_col += 1

    puzzle_printed: str = ""
    for row in range(N):
        line = ""
        for col in range(N):
            if puzzle[row][col] > 5:
                puzzle_is_unsolvable = True
            line += f'{puzzle[row][col]} '
        puzzle_printed += f"{line.strip()}\n"
    puzzle_printed = puzzle_printed.strip()

    if puzzle_is_unsolvable:
        print("The countdoku puzzle is unsolvable!")
    else:
        solution_output: str = f"""--Solution--

{puzzle_printed}

checks: {num_checks} backtracks: {num_backtracks}"""
        print(solution_output)

    x = 1


if __name__ == '__main__':
    main()