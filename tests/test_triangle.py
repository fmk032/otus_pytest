"""
Тесты для класса Triangle
"""
import pytest
from src.triangle import Triangle

# Тестируемые НЕ треугольники
not_triangles = [
    (1, 2, 3),
    (0, 3, 3)
]


def test_triangle_name(triangle):
    """Тест проверяет атрибут name объектов, генерируемых фикстурой triangle"""
    assert triangle.name == "TRIANGLE"


def test_triangle_area(triangle):
    """Тест проверяет метод area объектов, генерируемых фикстурой triangle"""
    side_a = triangle.side_a
    side_b = triangle.side_b
    side_c = triangle.side_c
    half_p = triangle.perimeter / 2
    assert triangle.area == (half_p * (half_p - side_a) * (half_p - side_b) * (half_p - side_c)) ** 0.5


def test_triangle_perimeter(triangle):
    """Тест проверяет метод perimeter объектов, генерируемых фикстурой triangle"""
    assert triangle.perimeter == triangle.side_a + triangle.side_b + triangle.side_c


@pytest.mark.parametrize("value", not_triangles)
def test_triangle_valid_sides_negative(value):
    """Тест проверяет ошибку при создании объекта класса Triangle с невалидными сторонами.
       Стороны (value) выбираются из числа тестируемых НЕ треугольников (not_triangles)"""
    with pytest.raises(ValueError):
        Triangle(value[0], value[1], value[2])
