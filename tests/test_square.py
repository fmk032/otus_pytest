"""
Тесты для класса Square
"""


def test_square_name(square):
    """Тест проверяет атрибут name объектов, генерируемых фикстурой square"""
    assert square.name == "SQUARE"


def test_square_area(square):
    """Тест проверяет метод area объектов, генерируемых фикстурой square"""
    assert square.area == square.side_a **2


def test_square_perimeter(square):
    """Тест проверяет метод perimeter объектов, генерируемых фикстурой square"""
    assert square.perimeter == square.side_a * 4
