"""
Модуль класса геометрической фигуры Круг
"""
import math
from src.figure import Figure


class Circle(Figure):
    """Класс геометрической фигуры Круг"""
    def __init__(self, radius):
        #super().__init__()
        self.radius = radius

    name = 'CIRCLE'

    @property
    def area(self):
        """Возвращает площадь (area) экземпляра класса Circle, вызывающего метод"""
        return math.pi * self.radius**2/2

    @property
    def perimeter(self):
        """Возвращает периметр (perimeter) экземпляра класса Circle, вызывающего метод"""
        return 2 * math.pi * self.radius
