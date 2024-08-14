import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, new_number",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("0987654321098765", "0987 65** **** 8765"),
        ("6279472307062356", "6279 47** **** 2356"),
        ("1234567890", "не корректно введен номер"),
        ("", "не корректно введен номер"),
    ],
)
def test_get_mask_card_number(card_number: str, new_number: str) -> None:
    """Тест функции маскитовки карты"""
    assert get_mask_card_number(card_number) == new_number


@pytest.mark.parametrize(
    "mask_account, new_mask_account",
    [
        ("12345678901234567890", "**7890"),
        ("87943067878376987769", "**7769"),
        ("87387697362864232343", "**2343"),
        ("1234567890", "не корректно введен номер"),
        ("", "не корректно введен номер"),
    ],
)
def test_get_mask_account(mask_account: str, new_mask_account: str) -> None:
    """Тест функции маскировки счета"""
    assert get_mask_account(mask_account) == new_mask_account
