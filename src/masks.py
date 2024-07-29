def get_mask_card_number(number: int) -> str:
    """Функция создания маски типа хххх хх** **** хххх для числа"""

    number_str = str(number)

    if len(number_str) != 16:
        return "не корректно введен номер"

    first_four = number_str[:4]
    second_four = number_str[4:6] + "*" * 2
    third_four = "*" * 4
    # Get the last four digits of the number
    last_four = number_str[-4:]

    return f"{first_four} {second_four} {third_four} {last_four}"


def get_mask_account(number: int) -> str:
    """Функция создания маски типа **хххх для числа"""

    number_str = str(number)
    last_chars = number_str[-4:]

    return f"**{last_chars}"
