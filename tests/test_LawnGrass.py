import pytest


def test_smartphone_init(product_grass_1):
    assert product_grass_1.name == "Газонная трава"
    assert product_grass_1.description == "Элитная трава для газона"
    assert product_grass_1.coast == 500.0
    assert product_grass_1.quantity == 20
    assert product_grass_1.country == "Россия"
    assert product_grass_1.germination_period == "7 дней"
    assert product_grass_1.color == "Зеленый"


def test_smartphone_add(product_grass_1, product_grass_2):
    assert product_grass_1 + product_grass_2 == 16750.0


def test_smartphone_add_false(product_grass_1, product_grass_2):
    with pytest.raises(TypeError):
        product_grass_1 + 1
