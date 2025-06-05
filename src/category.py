from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        """Конструктор класса Категории с аргументами: имя/описание/список_товаров"""

        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    @property
    def products(self):
        """Геттер получения продуктов"""

        return self.__products

    def add_product(self, product: Product):
        """Метод добавления нового продукта в приватный список продуктов"""

        self.__products.append(product)
        Category.product_count += 1

    @property
    def get_product(self):
        """Геттер для получения списка продуктов"""
        return self.__products

    @property
    def get_list_product(self):
        """Геттер для вывода списка продуктов из приватного списка"""

        product_list = ""
        for product in self.__products:
            product_list += f"{product.name}, {product.coast} руб. Остаток: {product.quantity} шт.\n"
        return product_list


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    # print(product1.product)
    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2])
    # print(category1)
    print(category1.get_list_product)
    print()
