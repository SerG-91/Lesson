list_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]


def filter_by_state(values: list, filter_by: str = "EXECUTED") -> list:
    """Функция фильтрации данных по ключу"""

    new_list = [i for i in values if i["state"] == filter_by]
    return new_list


print(filter_by_state(list_data, "EXECUTED"))


list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def sort_by_date(value: list, revers: bool = True) -> list:
    """Функция сортировки даты"""

    return sorted(value, reverse=revers, key=lambda x: x["date"])


print(sort_by_date(list))
