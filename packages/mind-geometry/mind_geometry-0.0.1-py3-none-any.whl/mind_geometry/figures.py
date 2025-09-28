from abc import ABC, abstractmethod
from math import pi, sqrt


class Figure(ABC):
    @abstractmethod
    def get_area(self, *args, **kwargs) -> float:
        pass


class Circle(Figure):
    def __init__(self, radius: float | int) -> None:
        self.radius = radius

    def get_area(self) -> float:
        return pi * self.radius ** 2


class Triangle(Figure):
    def __init__(self, a: float | int, b: float | int, c: float | int) -> None:
        """
        a, b, c - стороны треугольника
        p - полупериметр
        """
        self.a, self.b, self.c = sorted([a, b, c])
        self.p = (a + b + c) / 2

    def get_area(self) -> float:
        return sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))
    
    def is_right(self) -> bool:
        return pow(self.a, 2) + pow(self.b, 2) == pow(self.c, 2)



