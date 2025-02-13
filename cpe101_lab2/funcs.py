"""
funcs.py contains the functions written for CPE101 Lab 2
- Author: Logan Schmid
- Date Created: 2/11/25
"""

import math


def f(x: int) -> int:
    return 7 * x**2 + 2 * x


def g(x: int, y: int) -> float:
    if x == 0:
        raise ZeroDivisionError

    numerator: int = x**2 + y**2
    denominator: int = 3 * x
    return numerator / denominator


def hypotenuse(side1: int, side2: int) -> float:
    return math.sqrt(side1**2 + side2**2)


def is_positive(num: int) -> bool:
    return num >= 0