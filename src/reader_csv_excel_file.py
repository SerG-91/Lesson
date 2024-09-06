import logging
import os.path
from typing import Any

import pandas as pd

from config import DATA_PATH, LOGS_PATH

logs_path = os.path.join(LOGS_PATH, "logi.log")
logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(logs_path, mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def open_csv(file_name: str) -> Any:
    """Функция принимает на входе CSV файл и возвращает список словарей"""
    try:
        logger.info("Программа считывает файл")
        file_excel_path = os.path.join(DATA_PATH, file_name)
        transactions_df = pd.read_csv(file_excel_path, sep=";", decimal=",", encoding="utf-8")
        logger.info("Программа формирует список из файла")
        result = transactions_df.to_dict(orient="records")
        logger.info("Программа выводит полученый результат")
        return result
    except Exception as error:
        logger.error(f"При считывании файла произошла ошибка {error}.")


def open_excel(file_name: str) -> Any:
    """Функция принимает на входе EXCEL файл и возвращает список словарей"""
    try:
        logger.info("Старт формирования списка")
        file_excel_path = os.path.join(DATA_PATH, file_name)
        excel_data = pd.read_excel(file_excel_path)
        logger.info("Программа формирует список из файла")
        dict_list = excel_data.to_dict(orient="records")
        logger.info("Программа выводит полученый результат")
        return dict_list
    except Exception as error:
        logger.error(f"При считывании файла произошла ошибка {error}.")


# print(open_csv("transactions.csv"))
# print(open_excel("transactions_excel.xlsx"))
