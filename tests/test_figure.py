"""
Тесты для класса Figure
"""
import pytest
from src.triangle import Triangle
from src.rectangle import Rectangle
from src.square import Square
from src.circle import Circle


class SampleClass:
    """Класс для sampleObject - входных данных теста test_add_area_not_figure_negative"""


sampleObject = SampleClass()

# Тестируемые фигуры
figures = [
    Triangle(2,2,2),
    Rectangle(2,2),
    Square(2),
    Circle(2)
]

# Тестируемые НЕ фигуры
not_figures = [
    1,
    'string',
    sampleObject
]


@pytest.mark.parametrize("added_figure", figures)
@pytest.mark.parametrize("figure", figures)
def test_add_area(figure, added_figure):
    """Тест проверяет метод add_area объекта figure, принимающего added_figure.
    figure и added_figure выбираются из числа тестируемых фигур (figures)"""
    assert figure.add_area(added_figure) == figure.area + added_figure.area


@pytest.mark.parametrize("not_figure", not_figures)
@pytest.mark.parametrize("figure", figures)
def test_add_area_not_figure_negative(figure, not_figure):
    """Тест проверяет ошибку при вызове метода add_area объекта figure, принимающего not_figure.
    figure выбираются из числа тестируемых фигур (figures), not_figure из НЕ фигур (not_figures)"""
    with pytest.raises(ValueError):
        figure.add_area(not_figure)
