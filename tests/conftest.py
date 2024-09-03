import pytest

from src.utils import get_read_json


@pytest.fixture()
def data():
    return "11.03.2024"


@pytest.fixture()
def by_state():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture()
def by_date():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture()
def get_path():
    return "../data/operations.json"


@pytest.fixture()
def get_bed_path():
    return " "


@pytest.fixture
def transactions():
    return get_read_json('../data/operations.json')


@pytest.fixture
def id_number():
    return 441945886


