from unittest.mock import patch

import pytest

from src.reader_csv_excel_file import open_csv, open_excel


@patch("pandas.read_csv")
def test_open_csv(mock_read_csv):
    """Тестирование с помощю mock и patch считывания csv файла"""
    mock_read_csv.return_value.to_dict.return_value = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
        }
    ]
    result = open_csv("test_file.csv")
    assert result == [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
        }
    ]


@patch("pandas.read_excel")
def test_open_excel(mock_read_excel):
    """Тестирование с помощю mock и patch считывания excel файла"""
    mock_read_excel.return_value.to_dict.return_value = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
        }
    ]
    result = open_excel("test_file.xlsx")
    assert result == [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
        }
    ]


def test_open_csv_wrong_format():
    """Фуекция тестирования ошибок о неподдерживаемом формате файла"""
    with pytest.raises(Exception) as exc_info:
        open_csv("test.xlsx")
        assert str(exc_info.value) == "При считывании файла произошла ошибка."


def test_open_excel_wrong_format():
    """Фуекция тестирования ошибок о неподдерживаемом формате файла"""
    with pytest.raises(Exception) as exc_info:
        open_excel("test.csv")
        assert str(exc_info.value) == "При считывании файла произошла ошибка."
