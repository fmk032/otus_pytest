"""
Модуль класса геометрической фигуры Квадрат
"""
from src.rectangle import Rectangle


class Square(Rectangle):
    """Класс геометрической фигуры Квадрат"""
    def __init__(self, side):
        self.side_a = side
        self.side_b = side

    name = 'SQUARE'
