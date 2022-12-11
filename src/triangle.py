"""
Модуль класса геометрической фигуры Треугольник
"""
from src.figure import Figure


class Triangle(Figure):
    """Класс геометрической фигуры Треугольник"""
    def __init__(self, side_a, side_b, side_c):
        if side_a >= side_b + side_c or side_b >= side_a + side_c or side_c >= side_a + side_b:
            raise ValueError
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    name = 'TRIANGLE'

    @property
    def area(self):
        """Возвращает площадь (area) экземпляра класса Triangle, вызывающего метод"""
        half_p = self.perimeter/2
        return (half_p * (half_p - self.side_a) * (half_p - self.side_b) * (half_p - self.side_c)) ** 0.5

    @property
    def perimeter(self):
        """Возвращает периметр (perimeter) экземпляра класса Triangle, вызывающего метод"""
        return self.side_a + self.side_b + self.side_c
