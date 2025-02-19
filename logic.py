
def is_even(num: int) -> bool:
    return num % 2 == 0

def is_an_interval(num: int) -> bool:
    return ( ((2 <= num) and (num < 9))
            or ((47 < num) and (num < 92))
            or ((12 < num) and (num <= 19))
            or ((101 <= num) and (num <= 103)) )