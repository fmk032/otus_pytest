"""
Модуль класса геометрической фигуры Прямоугольник
"""
from src.figure import Figure


class Rectangle(Figure):
    """Класс геометрической фигуры Прямоугольник"""
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    name = 'RECTANGLE'

    @property
    def area(self):
        """Возвращает площадь (area) экземпляра класса Rectangle, вызывающего метод"""
        return self.side_a * self.side_b

    @property
    def perimeter(self):
        """Возвращает периметр (perimeter) экземпляра класса Rectangle, вызывающего метод"""
        return self.side_a * 2 + self.side_b * 2
