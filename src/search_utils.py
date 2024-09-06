import logging
import re
from collections import Counter
from typing import Any

from config import LOGS_PATH

logger = logging.getLogger("__name__")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(f"{LOGS_PATH}/logs_modul.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s %(funcName)s %(lineno)d: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

list_trans = [
    {
        "id": 441945886,
        "state": "AEXEC",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    },
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    },
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2018-03-23T10:45:06.972075",
        "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 214024827,
        "state": "EXECUTED",
        "date": "2018-12-20T16:43:26.929246",
        "operationAmount": {"amount": "70946.18", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 10848359769870775355",
        "to": "Счет 21969751544412966366",
    },
    {
        "id": 522357576,
        "state": "EXECUTED",
        "date": "2019-07-12T20:41:47.882230",
        "operationAmount": {"amount": "51463.70", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 48894435694657014368",
        "to": "Счет 38976430693692818358",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 596171168,
        "state": "EXECUTED",
        "date": "2018-07-11T02:26:18.671407",
        "operationAmount": {"amount": "79931.03", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Открытие вклада",
        "to": "Счет 72082042523231456215",
    },
    {
        "id": 716496732,
        "state": "EXECUTED",
        "date": "2018-04-04T17:33:34.701093",
        "operationAmount": {"amount": "40701.91", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Visa Gold 5999414228426353",
        "to": "Счет 72731966109147704472",
    },
    {
        "id": 863064926,
        "state": "EXECUTED",
        "date": "2019-12-08T22:46:21.935582",
        "operationAmount": {"amount": "41096.24", "currency": {"name": "USD", "code": "USD"}},
        "description": "Открытие вклада",
        "to": "Счет 90424923579946435907",
    },
]


def filter_by_description(data_list: list[dict], str_search: str) -> list[dict]:
    """Функция фильтрации данных по описанию"""
    new_list = []
    logger.info("Старт программы")
    if len(data_list) == 0:
        logger.error("ОШИБКА: Список пустой")
        exit("Работа программы завершена")
    elif len(str_search) == 0:
        logger.error("ОШИБКА: Поисковый запрос отсутствует")
        exit("Работа программы завершена")
    else:
        logger.info("Перебор списка словарей")
        for item in data_list:
            try:
                if re.search(str_search, item["description"]):
                    new_list.append(item)
            except Exception as ex:
                logger.error(f"ОШИБКА: {ex}")
    logger.info("Завершение программы и вывод результата")
    return new_list


# print(filter_by_description(list_trans, 'Открытие'))


def count_description(data_list: list[dict], list_category: list) -> Any:
    """Функция подсчета по описанию"""
    list_only_category = []
    result = []
    logger.info("Старт программы")
    try:
        if len(data_list) == 0 or len(list_category) == 0:
            logger.error("ОШИБКА: Список  или тритерии поиска пустые")

            exit("Даные или критерии не обнаружены.\nРабота программы завершена.")

        logger.info("Создаем список из описаний операций")

        for item in data_list:
            list_only_category.append(item["description"])
        logger.info("Сравниваем список категорий со списком критерий")

        for i in list_category:
            if i in list_only_category:
                result.append(i)
        counted = Counter(result)
        logger.info("Завершение программы и вывод результата")

        return counted
    except Exception as ex:
        logger.error(f"ОШИБКА: {ex}")



# print(count_description(list_trans, ['Перевод со счета на счет', 'Перевод с карты на карту']))
