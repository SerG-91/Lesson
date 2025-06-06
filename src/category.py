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
        Category.product_count += len(products) if products else []

    def __str__(self):
        all_coast = 0
        for product in self.__products:
            all_coast += product.quantity
        return f"{self.name}, количество продуктов: {all_coast} шт."

    @property
    def products(self):
        """Геттер получения продуктов"""

        return self.__products

    def add_product(self, product: Product):
        """Метод добавления нового продукта в приватный список продуктов"""
        if isinstance(product, Product):
            self.get_product.append(product)
            Category.product_count += 1
        else:
            raise TypeError

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
