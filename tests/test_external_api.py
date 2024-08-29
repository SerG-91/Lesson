from src.external_api import convert_from_to_rub
from unittest.mock import patch


@patch('requests.get')
def test_convert_from_to_rub(mock_get):
    mock_get.return_value.json.return_value = {"result": 10}
    assert convert_from_to_rub({
        "operationAmount":
            {"amount": "31957.58",
             "currency": {
                 "code": "USD"}
             }
                                }) == 10
