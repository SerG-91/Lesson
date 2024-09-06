from src.utils import get_read_json, transaction_amount


def test_get_read_json(get_path):
    assert get_read_json(get_path)[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }


def test_get_read_json_null(get_bed_path):
    assert get_read_json(get_bed_path) == []


def test_transaction_amount(transactions, id_number):
    assert transaction_amount(transactions, id_number) == "31957.58"



