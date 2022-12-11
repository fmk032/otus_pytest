"""
Тесты для класса Rectangle
"""


def test_rectangle_name(rectangle):
    """Тест проверяет атрибут name объектов, генерируемых фикстурой rectangle"""
    assert rectangle.name == "RECTANGLE"


def test_rectangle_area(rectangle):
    """Тест проверяет метод area объектов, генерируемых фикстурой rectangle"""
    assert rectangle.area == rectangle.side_a * rectangle.side_b


def test_rectangle_perimeter(rectangle):
    """Тест проверяет метод perimeter объектов, генерируемых фикстурой rectangle"""
    assert rectangle.perimeter == (rectangle.side_a + rectangle.side_b) * 2
