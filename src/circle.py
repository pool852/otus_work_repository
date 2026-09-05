import math

from src.figure import Figure


class Circle(Figure):

    def __init__(self, side_r: int):
        if side_r <= 0:
            raise ValueError("It is impossible to draw a circle with a negative or zero radius")
        self.side_r = side_r

    @property
    def area(self):
        return (self.side_r ** 2) * math.pi

    @property
    def perimeter(self):
        return self.side_r * math.pi * 2
