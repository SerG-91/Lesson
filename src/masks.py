def get_mask_card_number(number: str) -> str:
    """Функция создания маски типа хххх хх** **** хххх для числа"""

    if len(str(number)) != 16:
        return "не корректно введен номер"
    else:
        first_four = number[:4]
        second_four = number[4:6] + "*" * 2
        third_four = "*" * 4
        # Get the last four digits of the number
        last_four = number[-4:]
        return f"{first_four} {second_four} {third_four} {last_four}"


def get_mask_account(number: str) -> str:
    """Функция создания маски типа **хххх для числа"""

    if len(str(number)) < 20:
        return "не корректно введен номер"
    else:
        number_str = str(number)
        last_chars = number_str[-4:]
        return f"**{last_chars}"


print(get_mask_card_number("1234567890123456"))
print(get_mask_account("12345678901234567890"))
