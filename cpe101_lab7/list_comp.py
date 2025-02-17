from objects import *
from funcs_objects import distance

def distance_all(points: list[Point]) -> list[float]:
    return [distance(point, Point(0, 0)) for point in points]


def are_in_first_quadrant(points: list[Point]) -> list[Point]:
    return [point for point in points if point.x >= 0 and point.y >= 0]

