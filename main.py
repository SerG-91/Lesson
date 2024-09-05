# import src.masks
#
# number_card = "1323098667808976"
# number_score = "8369878934"
# print(src.masks.get_mask_card_number(number_card))
# print(src.masks.get_mask_account(number_score))
import os

from config import DATA_PATH
from src.processing import filter_by_state, sort_by_date
from src.reader_csv_excel_file import open_csv, open_excel
from src.search_utils import filter_by_description
from src.utils import get_read_json
from src.widget import mask_account_card, get_data

text_choice = ("1. Получить информацию о транзакциях из JSON-файла\n2. Получить информацию о транзакциях из "
               "CSV-файла\n3. Получить информацию о транзакциях из XLSX-файла")
list_status = ["EXECUTED", "CANCELED", "PENDING"]
filename_list = ["operations.json", "transactions.csv", "transactions_excel.xlsx"]
answer_list = {
    '1': 'JSON-файл', '2': 'CSV-файл', '3': 'XLSX-файл'
}


def main():
    n = 0
    loader_data = []
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями. Выберите необходимый пункт меню:")
    choice_user = input(f"{text_choice}\n")
    while answer_list.keys() != choice_user:  # Обработка введеного пользователем пункта
        if choice_user in answer_list:
            print(f"Для обработки выбран {answer_list[choice_user]}")
            break
        else:
            choice_user = input(
                f"Выбор некорректен, попробуйте ещё раз ввести номер необходимого пункта:\n{text_choice}"
                f" \n")  # Постоянно запрашивает номер пункта пока он не будет корректным
    if choice_user == list(answer_list.keys())[0]:
        data_path = os.path.join(DATA_PATH, filename_list[0])
        loader_data = get_read_json(data_path)  #Возвращает сформированный JSON файл по его пути
        n = 1
    elif choice_user == list(answer_list.keys())[1]:
        data_path = os.path.join(DATA_PATH, filename_list[1])
        loader_data = open_csv(data_path)  #Возвращает сформированный CSV файл по его пути
    elif choice_user == list(answer_list.keys())[2]:
        data_path = os.path.join(DATA_PATH, filename_list[2])
        loader_data = open_excel(data_path)  #Возвращает сформированный EXCEL файл по его пути
    status_for_filter = input(
        f"Введите статус по которому необходимо выполнить фильтрацию.\n-> "
        f"Доступные для фильтровки статусы: {list_status[0]}, {list_status[1]}, {list_status[2]}\n-> ").upper()
    while status_for_filter not in list_status:
        status_for_filter = input(
            f"Статус операции {status_for_filter} недоступен.\n"
            f"Введите статус по которому необходимо выполнить фильтрацию.\n"
            f"Доступные для фильтровки статусы: {list_status[0]}, {list_status[1]}, {list_status[2]}\n-> ").upper()
    transactions_by_status = filter_by_state(loader_data, status_for_filter) # Возвращает отсортированный список по ключу пользователя
    for item in transactions_by_status:   # Возвращает замаскированые счета и карты
        try:
            item['from'] = mask_account_card(str(item.get('from')))
            item['to'] = mask_account_card(str(item.get('to')))
            item['date'] = get_data(str(item.get('date')))
        except Exception as ex:
            pass
    ###########################
    answer_sort_by_data = input('Отсортировать операции по дате? Да/Нет\n-> ').lower()
    if answer_sort_by_data == "да":   # Сортировка по дате при ответе - да
        answer_sort_by_data_vector = input('Отсортировать по возрастанию или по убыванию\n-> ').lower()
        if answer_sort_by_data_vector == 'возрастанию': # Сортировка по возрастающей дате
            transactions_by_status = sort_by_date(transactions_by_status, revers=False)
        elif answer_sort_by_data_vector == 'убыванию':  # Сортировка по убывающей дате
            transactions_by_status = sort_by_date(transactions_by_status)
        else:
            print('Не корректно введено условие сортировки. Список небыл отсортирован.')
    elif answer_sort_by_data == "нет":
        print('Список небыл отсортирован по дате')
    else:
        print('Вы не ввели нужного ответа. Список небыл отсортирован')
    ###
    answer_filter_by_rub = input('Выводить только рублевые тразакции? Да/Нет\n-> ').lower()
    transactions_by_ryb = []
    if answer_filter_by_rub == 'да':
        if n == 1:
            for item in transactions_by_status:
                if item["operationAmount"]["currency"]["code"] == "RUB":
                    transactions_by_ryb.append(item)
        else:
            for item in transactions_by_status:
                if item["currency_code"] == "RUB":
                    transactions_by_ryb.append(item)
    else:
        transactions_by_ryb = transactions_by_status
    # print(transactions_by_ryb)
    ####
    answer_filter_by_description = input("Отфильтровать список транзакций по определенному слову в описании? "
                                         "Да/Нет\n-> ").lower()
    if answer_filter_by_description == 'да':
        description_words = input("Введите слова\n-> ")
        transactions_by_ryb = filter_by_description(transactions_by_ryb, description_words)
    for item in transactions_by_ryb:
        if n == 1:
            result_data = item['date']
            result_description = item['description']
            result_from = item['from']
            result_to = item['to']
            result_amount = item['operationAmount']['amount']
            if result_description == "Открытие вклада":
                print(f'{result_data}, {result_description}\n{result_to}\nСумма: {result_amount}\n\n')
            else:
                print(f'{result_data}, {result_description}\n{result_from} -> {result_to}\nСумма: {result_amount}\n\n')
        else:
            result_data = item['date']
            result_description = item['description']
            result_from = item['from']
            result_to = item['to']
            result_amount = item['amount']
            if result_description == "Открытие вклада":
                print(f'{result_data}, {result_description}\n{result_to}\nСумма: {result_amount}\n\n')
            else:
                print(f'{result_data}, {result_description}\n{result_from} -> {result_to}\nСумма: {result_amount}\n\n')

    # print(result)




if __name__ == '__main__':
    main()


# print(main())
