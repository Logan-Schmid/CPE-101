from objects import Point, Circle
from math import sqrt

def distance(point1: Point, point2: Point) -> float:
    return sqrt( (point1.x - point2.x)**2 + (point1.y - point2.y)**2 )


def circles_overlap(circle1: Circle, circle2: Circle) -> bool:
    return distance(circle1.center, circle2.center) < (circle1.radius + circle2.radius)