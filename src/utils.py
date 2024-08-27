import json
from typing import Any

from src.external_api import convert_from_eur_to_rub, convert_from_usd_to_rub


def get_read_json(data: str) -> Any:
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(data, "r", encoding="utf-8") as f:
            new_data = json.load(f)
            if not new_data or not isinstance(new_data, list):
                return []
            return new_data
    except json.JSONDecodeError:
        return "Invalid JSON data"
    except FileNotFoundError:
        return []


def transaction_amount(transactions: dict, transaction_id: int) -> Any:
    """Функция принимает на вход список транзакций и id транзакции которую необходимо конвертировать и
    возвращает транзакцию в рублях"""
    for trans in transactions:
        if trans.get("id") == transaction_id:
            if trans["operationAmount"]["currency"]["code"] == "RUB":
                amount = trans["operationAmount"]["amount"]
                return amount
            elif trans["operationAmount"]["currency"]["code"] == "USD":
                usd_amount = trans["operationAmount"]["amount"]
                rub_amount = convert_from_usd_to_rub(usd_amount)
                return round(rub_amount, 3)
            elif trans["operationAmount"]["currency"]["code"] == "EUR":
                eur_amount = trans["operationAmount"]["amount"]
                rub_amount = convert_from_eur_to_rub(eur_amount)
                return round(rub_amount, 3)


src_data = "../data/operations.json"

print(get_read_json(src_data))

transactions_list = get_read_json(src_data)

print(transaction_amount(transactions_list, 939719570))
