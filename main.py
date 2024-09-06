import logging
import os

from config import DATA_PATH, LOGS_PATH
from src.processing import filter_by_state, sort_by_date
from src.reader_csv_excel_file import open_csv, open_excel
from src.search_utils import filter_by_description
from src.utils import get_read_json
from src.widget import get_data, mask_account_card

logger = logging.getLogger("__name__")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"{LOGS_PATH}/main.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s %(funcName)s %(lineno)d: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

text_choice = (
    "1. Получить информацию о транзакциях из JSON-файла\n2. Получить информацию о транзакциях из "
    "CSV-файла\n3. Получить информацию о транзакциях из XLSX-файла"
)
list_status = ["EXECUTED", "CANCELED", "PENDING"]
filename_list = ["operations.json", "transactions.csv", "transactions_excel.xlsx"]
answer_list = {"1": "JSON-файл", "2": "CSV-файл", "3": "XLSX-файл"}


def main() -> None:
    logger.info("Старт программы")
    n = 0
    loader_data = []
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями. Выберите необходимый пункт меню:")
    choice_user = input(f"{text_choice}\n")
    while answer_list.keys() != choice_user:  # Обработка введеного пользователем пункта
        if choice_user in answer_list:
            print(f"Для обработки выбран {answer_list[choice_user]}")
            logger.info(f"Пользователь выбрал вариант {choice_user}")
            break
        else:
            choice_user = input(
                f"Выбор некорректен, попробуйте ещё раз ввести номер необходимого пункта:\n{text_choice}" f" \n"
            )  # Постоянно запрашивает номер пункта пока он не будет корректным
            logger.info("Пользователь повторно выбирает пункт меню")
    logger.info("Начато считывание данных из файла")
    if choice_user == list(answer_list.keys())[0]:
        data_path = os.path.join(DATA_PATH, filename_list[0])
        loader_data = get_read_json(data_path)  # Возвращает сформированный JSON файл по его пути
        n = 1
    elif choice_user == list(answer_list.keys())[1]:
        data_path = os.path.join(DATA_PATH, filename_list[1])
        loader_data = open_csv(data_path)  # Возвращает сформированный CSV файл по его пути
    elif choice_user == list(answer_list.keys())[2]:
        data_path = os.path.join(DATA_PATH, filename_list[2])
        loader_data = open_excel(data_path)  # Возвращает сформированный EXCEL файл по его пути
    status_for_filter = input(
        f"Введите статус по которому необходимо выполнить фильтрацию.\n-> "
        f"Доступные для фильтровки статусы: {list_status[0]}, {list_status[1]}, {list_status[2]}\n-> "
    ).upper()
    logger.info(f"Пользователь выбрал вариант фильтра -> {status_for_filter}")
    while status_for_filter not in list_status:
        status_for_filter = input(
            f"Статус операции {status_for_filter} недоступен.\n"
            f"Введите статус по которому необходимо выполнить фильтрацию.\n"
            f"Доступные для фильтровки статусы: {list_status[0]}, {list_status[1]}, {list_status[2]}\n-> "
        ).upper()
        logger.info("Пользователь повторно выбирает вариант фильтра")
    transactions_by_status = filter_by_state(
        loader_data, status_for_filter
    )  # Возвращает отсортированный список по ключу пользователя
    logger.info("Происходит маскировка счетов и карт")
    for item in transactions_by_status:  # Возвращает замаскированые счета и карты
        try:
            item["from"] = mask_account_card(str(item.get("from")))
            item["to"] = mask_account_card(str(item.get("to")))
            item["date"] = get_data(str(item.get("date")))
        except Exception as ex:
            logger.error(f"Произошла ошибка {ex}")
    logger.info("Маскировка счетов и карт выполнена")
    ###########################
    answer_sort_by_data = input("Отсортировать операции по дате? Да/Нет\n-> ").lower()
    logger.info(f"Пользователь согласился с сортировкой по дате -> {answer_sort_by_data}")
    if answer_sort_by_data == "да":  # Сортировка по дате при ответе - да
        answer_sort_by_data_vector = input("Отсортировать по возрастанию или по убыванию\n-> ").lower()
        if answer_sort_by_data_vector == "возрастанию":  # Сортировка по возрастающей дате
            transactions_by_status = sort_by_date(transactions_by_status, revers=False)
        elif answer_sort_by_data_vector == "убыванию":  # Сортировка по убывающей дате
            transactions_by_status = sort_by_date(transactions_by_status)
            logger.info("Список был отсортирован по дате")
        else:
            print("Не корректно введено условие сортировки. Список небыл отсортирован.")
            logger.info("Список не был отсортирован по дате")
    elif answer_sort_by_data == "нет":
        print("Список небыл отсортирован по дате")
        logger.info("Список не был отсортирован по дате")
    else:
        print("Вы не ввели нужного ответа. Список небыл отсортирован")
        logger.info("Список не был отсортирован по дате")
    ###
    answer_filter_by_rub = input("Выводить только рублевые тразакции? Да/Нет\n-> ").lower()
    logger.info(f"Пользователь выбрал выводить только рублевые транзакции -> {answer_filter_by_rub}")
    transactions_by_ryb = []
    if answer_filter_by_rub == "да":
        if n == 1:
            for item in transactions_by_status:
                if item["operationAmount"]["currency"]["code"] == "RUB":
                    transactions_by_ryb.append(item)
        else:
            for item in transactions_by_status:
                if item["currency_code"] == "RUB":
                    transactions_by_ryb.append(item)
        logger.info("Выбраны только рублевые транзакции")
    else:
        transactions_by_ryb = transactions_by_status
        logger.info("Выбраны все транзакции")
    ####
    answer_filter_by_description = input(
        "Отфильтровать список транзакций по определенному слову в описании? " "Да/Нет\n-> "
    ).lower()
    logger.info(f"Пользователь согласился с выводом транзакций по критерию -> {answer_filter_by_description}")
    if answer_filter_by_description == "да":
        description_words = input("Введите слова\n-> ")
        transactions_by_ryb = filter_by_description(transactions_by_ryb, description_words)
        logger.info(f"Выбраны транзакции по критерию -> {description_words}")
    print(f"Всего банковских операций в выборке: {len(transactions_by_ryb)}\n")
    logger.info("Формирование финального списка")
    for item in transactions_by_ryb:
        if n == 1:
            result_data = item["date"]
            result_description = item["description"]
            result_from = item["from"]
            result_to = item["to"]
            result_amount = item["operationAmount"]["amount"]
            if result_description == "Открытие вклада":
                print(f"{result_data}, {result_description}\n{result_to}\nСумма: {result_amount}\n\n")
            else:
                print(f"{result_data}, {result_description}\n{result_from} -> {result_to}\nСумма: {result_amount}\n\n")
            # logger.info("Финальный список с формирован и выведен")
        else:
            result_data = item["date"]
            result_description = item["description"]
            result_from = item["from"]
            result_to = item["to"]
            result_amount = item["amount"]
            if result_description == "Открытие вклада":
                print(f"{result_data}, {result_description}\n{result_to}\nСумма: {result_amount}\n\n")
            else:
                print(f"{result_data}, {result_description}\n{result_from} -> {result_to}\nСумма: {result_amount}\n\n")
    logger.info("Финальный список с формирован и выведен")

    logger.info("Программа завершена")


if __name__ == "__main__":
    main()
