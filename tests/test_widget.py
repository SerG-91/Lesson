import pytest

from src.widget import get_data, mask_account_card


@pytest.mark.parametrize(
    "account_card, new_account_card",
    [
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ],
)
def test_mask_account_card(account_card: str, new_account_card: str) -> None:
    """Тест функции маскировки"""
    assert mask_account_card(account_card) == new_account_card


def test_get_data(data: str) -> None:
    """Тест функции маскироки даты"""
    assert get_data("2024-03-11T02:26:18.671407") == data
