
def max_101(num1: int, num2: int) -> int:
    return num1 if num1 > num2 else num2

def max_of_three(num1: float, num2: float, num3: float) -> float:
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

def rental_late_fee(days_late: int) -> int:
    if days_late > 24:
        return 100
    elif days_late > 15:
        return 19
    elif days_late > 9:
        return 7
    elif days_late > 0:
        return 5
    else:
        return 0







