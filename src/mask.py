"""Модуль маскировки карт и счетов"""


def mask_card_number(number: str) -> str:
    """Функция принимает строку с номером карты и возвращает ее в формате:
    XXXX XX** **** XXXX"""
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
    return "**" + number[-4:]


if __name__ == "__main__":
    card_num = "6831982476737658"
    account_num = "73654108430135874305"

    print(mask_card_number(card_num))
    print(mask_account_number(account_num))
