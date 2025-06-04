

def test_init(product):
    assert product.name == "Свинина"
    assert product.description == "Свинная продукция"
    assert product.price == 550.5
    assert product.quantity == 22