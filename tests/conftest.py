import pytest

from src.category import Category
from src.product import Product

@pytest.fixture
def category1():
    return Category(
        name="Рыба",
        description="Речная рыба",
        products=[
            Product("Окунь", "Речная рыба", 50.5, 3),
            Product("Елец", "Речная рыба", 40.3, 19),
            Product("Щука", "Речная рыба", 63.7, 11)
        ]
    )

@pytest.fixture
def category2():
    return Category(
        name="Мясо",
        description="Мясная продукция",
        products=[
            Product("Свинина", "Свинная продукция", 550.5, 22),
            Product("Говядина", "Говяжя продукция", 640.3, 19),
        ]
    )

@pytest.fixture
def product():
    return Product(
        name="Свинина",
        description="Свинная продукция",
        price=550.5,
        quantity=22
    )