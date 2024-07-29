from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(str_data: str) -> str:
    """Функция создания маски для счета"""
    if "Счет" in str_data:
        card = get_mask_account(str_data[-20:])
        new_card = str_data.replace(str_data[-20:], card)
        return new_card
    else:
        card = get_mask_card_number(str_data[-16:])
        new_card = str_data.replace(str_data[-16:], card)
        return new_card


def get_data(data: str) -> str:
    """Функция формата даты"""
    return f"{data[8:10]}.{data[5:7]}.{data[:4]}"


print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(get_data("2024-03-11T02:26:18.671407"))
