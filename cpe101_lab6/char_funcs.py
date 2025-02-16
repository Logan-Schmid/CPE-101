
def is_lower_101(char: str) -> bool:
    if not char:
        return False

    return ord('a') <= ord(char) <= ord('z')


def char_rot_13(char: str) -> str:
    if char.islower():
        rot_ascii_ind_above_lower_a: int = (ord(char) % ord('a')) + 13
        rot_ascii_ind: int = ord('a') + (rot_ascii_ind_above_lower_a % (ord('z') - ord('a') + 1))
        return chr(rot_ascii_ind)
    elif char.isupper():
        rot_ascii_ind_above_upper_a: int = (ord(char) % ord('A')) + 13
        rot_ascii_ind: int = ord('A') + (rot_ascii_ind_above_upper_a % (ord('Z') - ord('A') + 1))
        return chr(rot_ascii_ind)
    else:
        return char
