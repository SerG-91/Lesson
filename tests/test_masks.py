from src.masks import get_mask_account, get_mask_card_number

def test_get_mask_card_number():
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"
    assert get_mask_card_number("1234567890") == "не корректно введен номер"
    assert get_mask_card_number("") == "не корректно введен номер"


def test_get_mask_account():
    assert get_mask_account("12345678901234567890") == "**7890"
    assert get_mask_account("542355") == "не корректно введен номер"