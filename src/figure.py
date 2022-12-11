"""
Модуль класса геометрической фигуры
"""


class Figure:
    """Класс геометрической фигуры"""
    def __init__(self):
        self.area = None

    def add_area(self, figure):
        """Принимает figure (экземпляр класса какой-либо фигуры - класса Figure или наследника),
        возвращает сумму площадей (атрибутов area) объекта, вызывающего метод, и figure"""
        if not isinstance(figure, Figure):
            raise ValueError
        return self.area + figure.area
