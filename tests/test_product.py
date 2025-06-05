from src.product import Product


def test_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера продукция"
    assert product.coast == 180000.0
    assert product.quantity == 5


def test_create_new_product(dict_product, category1):
    new_product = Product.new_product(dict_product, category1.get_product)
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.coast == 180000.0
    assert new_product.quantity == 10


# def test_change_coast(product):
#     product.coast = 800
#     assert product.coast == 800
#     product.coast = 50
#     assert product.coast == 50


def test_coast_below_zero(product):
    product.coast = -10
    assert product.coast == 180000.0

