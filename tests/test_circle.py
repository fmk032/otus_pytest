"""
Тесты для класса Circle
"""
import math


def test_circle_name(circle):
    """Тест проверяет атрибут name объектов, генерируемых фикстурой circle"""
    assert circle.name == "CIRCLE"


def test_circle_area(circle):
    """Тест проверяет метод area объектов, генерируемых фикстурой circle"""
    assert circle.area == math.pi * circle.radius**2/2


def test_circle_perimeter(circle):
    """Тест проверяет метод perimeter объектов, генерируемых фикстурой circle"""
    assert circle.perimeter == 2 * math.pi * circle.radius
