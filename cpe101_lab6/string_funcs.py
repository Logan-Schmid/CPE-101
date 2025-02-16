
from char_funcs import char_rot_13

def str_rot_13(input_str: str) -> str:
    return ''.join([char_rot_13(letter) for letter in input_str])


def str_translate_101(input_str: str, old_char: str, new_char) -> str:
    new_str: list[str] = []

    for char in input_str:
        if char == old_char:
            char = new_char
        new_str.append(char)

    return ''.join(new_str)