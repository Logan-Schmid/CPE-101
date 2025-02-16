
def are_positive(input_list: list[int]) -> list[int]:
    return [value for value in input_list if value >= 0]


def are_greater_than_n(input_list: list[int], n: int) -> list[int]:
    return list(filter(lambda x: x > n, input_list))


def are_divisible_by_n(input_list: list[int], n: int) -> list[int]:
    divisible_by_n: list[int] = []
    for num in input_list:
        if num % n == 0:
            divisible_by_n.append(num)

    return divisible_by_n