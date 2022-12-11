"""
Фикстуры и входные данные для тестов
"""
import pytest
from src.triangle import Triangle
from src.rectangle import Rectangle
from src.square import Square
from src.circle import Circle

# Тестируемые треугольники
triangles = [
    (2, 3, 4),
    (2, 2, 3),
    (3, 3, 3)
]

# Тестируемые прямоугольники
rectangles = [
    (2, 3),
    (3, 3),
    (0, 3)
]

# Тестируемые квадраты
squares = [2, 3, 0]

# Тестируемые круги
circles = [2, 3, 0]


@pytest.fixture(params=triangles)
def triangle(request):
    """Фикструра принимает параметры triangles, генерирует и возвращает объекты класса Triangle"""
    side_a = request.param[0]
    side_b = request.param[1]
    side_c = request.param[2]
    yield Triangle(side_a, side_b, side_c)


@pytest.fixture(params=rectangles)
def rectangle(request):
    """Фикструра принимает параметры rectangles, генерирует и возвращает объекты класса Rectangle"""
    side_a = request.param[0]
    side_b = request.param[1]
    yield Rectangle(side_a, side_b)


@pytest.fixture(params=squares)
def square(request):
    """Фикструра принимает параметры squares, генерирует и возвращает объекты класса Square"""
    yield Square(request.param)


@pytest.fixture(params=circles)
def circle(request):
    """Фикструра принимает параметры circles, генерирует и возвращает объекты класса Circle"""
    yield Circle(request.param)
