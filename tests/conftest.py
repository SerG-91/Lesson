import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def category1():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        ]
    )


@pytest.fixture
def category2():
    return Category(
        name="Телевизоры",
        description="Телевизоры, как средство для удобства жизни",
        products=[
            Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
        ]
    )


@pytest.fixture
def product():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера продукция",
        price=180000.0,
        quantity=5
    )


@pytest.fixture
def dict_product():
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    }
