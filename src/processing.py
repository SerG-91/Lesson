# list_data = [
#     {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
#      'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
#      'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'},
#     {'id': 41428829, 'state': 'sdfg', 'date': '2019-07-03T18:35:29.512364',
#      'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
#      'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'},
#     {'id': 939719570, 'state': 'ee', 'date': '2018-06-30T02:08:58.425572',
#      'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
#      'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}
# ]


def filter_by_state(values: list, filter_by: str = "EXECUTED") -> list:
    """Функция фильтрации данных по ключу"""

    new_list = [i for i in values if i.get("state") == filter_by]
    return new_list


# print(filter_by_state(list_data, "ee"))


# list = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
# ]


def sort_by_date(value: list, revers: bool = True) -> list:
    """Функция сортировки даты"""

    return sorted(value, reverse=revers, key=lambda x: x["date"])

#
# print(sort_by_date(list))
