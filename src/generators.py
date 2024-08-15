from typing import Any


def filter_by_currency(transactions: list, currency_code: str = "USD") -> Any:
    """Функция выдает список транзакции, где валюта соответствует заданной."""

    if transactions == []:
        yield ("Нет транзакций")
    for i in transactions:
        if i["operationAmount"]["currency"]["code"] == currency_code:
            yield i
        else:
            yield ("Транзакции с таким кодом нет")


def transaction_descriptions(transactions: list) -> Any:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""

    if not transactions:
        yield "Нет транзакций"
    for description_operation in transactions:
        yield description_operation["description"]


def card_number_generator(start: int, stop: int) -> Any:
    """Функция может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999."""

    for x in range(start, stop + 1):
        number_zero = "0000000000000000"
        card_number = number_zero[: -len(str(x))] + str(x)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
