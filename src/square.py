"""
Модуль класса геометрической фигуры Квадрат
"""
from src.rectangle import Rectangle


class Square(Rectangle):
    """Класс геометрической фигуры Квадрат"""
    def __init__(self, side):
        super().__init__(side_a=side, side_b=side)

    name = 'SQUARE'
