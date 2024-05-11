"""Модуль маскировки карт и счетов"""


def mask_card_number(number: str) -> str:
    """Функция принимает строку с номером карты и возвращает ее в формате:
    XXXX XX** **** XXXX"""
    if type(number) is not str:
        raise TypeError("Ожидается строка")
    if not number.isdigit() or len(number) != 16:
        raise ValueError("Должно быть только 16 цифр")

    mask_number = number[:6] + "*" * 6 + number[-4:]

    string_to_return = ""
    block_counter = 0

    for digit in mask_number:
        block_counter += 1
        if block_counter <= 4:
            string_to_return += digit
        else:
            string_to_return += " " + digit
            block_counter = 1

    return string_to_return


def mask_account_number(number: str) -> str:
    """Функция принимает строку с номером счета и возвращает ее в формате: **XXXX"""
    if type(number) is not str:
        raise TypeError("Ожидается строка")
    if not number.isdigit() or len(number) != 20:
        raise ValueError("Должно быть только 20 цифр")

    return "**" + number[-4:]
