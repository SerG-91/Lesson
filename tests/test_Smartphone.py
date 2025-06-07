import pytest


def test_smartphone_init(product_smartphone_1):
    assert product_smartphone_1.name == "Iphone 15"
    assert product_smartphone_1.description == "512GB, Gray space"
    assert product_smartphone_1.coast == 210000.0
    assert product_smartphone_1.quantity == 8
    assert product_smartphone_1.efficiency == 98.2
    assert product_smartphone_1.model == "15"
    assert product_smartphone_1.memory == 512
    assert product_smartphone_1.color == "Gray space"


def test_smartphone_add(product_smartphone_1, product_smartphone_2):
    assert product_smartphone_1 + product_smartphone_2 == 2580000.0


def test_smartphone_add_false(product_smartphone_1):
    with pytest.raises(TypeError):
        product_smartphone_1 + 1
