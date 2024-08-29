from src.external_api import convert_from_usd_to_rub
from unittest.mock import patch


@patch("src.utils.convert_from_usd_to_rub")
def test_convert_from_usd_to_rub(mock_get):
    mock_get.return_value = {"result": 10}
    assert convert_from_usd_to_rub(10) == 10
    mock_get.assert_called_once_with("https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=10")
#


