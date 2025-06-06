import pytest

from src.category import Category


def test_init(category1, category2):
    assert category1.name == "Смартфоны"
    assert category2.name == "Телевизоры"

    assert category1.category_count == 2
    assert category2.category_count == 2
    assert Category.category_count == 2
    assert category1.product_count == 3
    assert category2.product_count == 3
    assert Category.product_count == 3


def test_get_list_product(category1):
    assert category1.get_list_product == ("Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\nIphone 15, "
                                          "210000.0 руб. Остаток: 8 шт.\n")


def test_str(category1):
    assert str(category1) == "Смартфоны, количество продуктов: 13 шт."


def test_add_product_error(category1, product):
    with pytest.raises(TypeError):
        category1.add_product(1)


def test_add_product(category1, product):
    category1.add_product(product)
    assert category1.products[-1].name == "Samsung Galaxy S23 Ultra"

