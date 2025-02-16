
def square_all(values: list[int]) -> list[int]:
    sq_func = lambda x: x ** 2
    squares: list[int] = list(map(sq_func, values))
    return squares


def add_n_all(my_list: list[int], n: int) -> list[int]:
    return [my_list[i] + n for i in range(len(my_list))]


def even_or_odd_all(my_list: list) -> list[bool]:
    i = 0
    while i < len(my_list):
        my_list[i] = True if my_list[i] % 2 == 0 else False
        i += 1

    return my_list