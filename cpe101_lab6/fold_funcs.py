
def sum2(input_list: list[int]) -> int:
    my_sum: int = 0
    for num in input_list:
        my_sum += num

    return my_sum


def index_of_smallest(input_list: list[int]) -> int:
    if not input_list:
        return -1
    if len(input_list) == 1:
        return 0

    index_smallest: int = 0
    current_min: int = input_list.pop(0)
    for index, num in enumerate(input_list):
        if num < current_min:
            index_smallest = index + 1
            current_min = num

    return index_smallest
