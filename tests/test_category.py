from src.category import Category


def test_init(category1, category2):
    assert category1.name == "Рыба"
    assert category2.name == "Мясо"

    assert category1.category_count == 2
    assert category2.category_count == 2
    assert Category.category_count == 2
    assert category1.product_count == 5
    assert  category2.product_count == 5
    assert Category.product_count == 5