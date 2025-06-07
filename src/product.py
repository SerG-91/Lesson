from src.BaseProduct import BaseProduct
from src.PrintMixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Конструктор класса с аргументами: имя/описание/цена/количество"""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        if self.quantity != 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт"

    def __add__(self, other):
        if type(other) is Product:
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, dict_product, get_product):
        """Класс-метод по созданию нового продукта исключающий дубликаты имен"""

        for product in get_product:
            if dict_product["name"] == product.name:
                dict_product["quantity"] += product.quantity
                if dict_product["price"] > product.__price:
                    return cls(dict_product["name"], dict_product["description"], dict_product["price"],
                               dict_product["quantity"])
                return cls(dict_product["name"], dict_product["description"], product.__price,
                           dict_product["quantity"])
            return cls(dict_product["name"], dict_product["description"], dict_product["price"],
                       dict_product["quantity"])

    @property
    def coast(self):
        return self.__price

    @coast.setter
    def coast(self, price: int):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if price < self.__price:
            choice = input("YES(y) / NO(n)")
            if choice == 'y':
                self.__price = price
        self.__price = self.__price
