import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("api_key")


def convert_from_to_rub(transaction: Any) -> Any:
    """Функция конвертации в рубли"""
    amount = transaction["operationAmount"]["amount"]
    code = transaction["operationAmount"]["currency"]["code"]
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}"
    headers = {"apikey": api_key}
    payload = {}  # type: dict
    response = requests.get(url, headers=headers, data=payload)
    print(response)
    return response.json()["result"]
