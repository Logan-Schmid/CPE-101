from typing import Self
from math import isclose

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __eq__(self, other: Self) -> bool:
        return isclose(self.x, other.x) and isclose(self.y, other.y)


class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    def __eq__(self, other) -> bool:
        return self.center == other.center and isclose(self.radius, other.radius)
