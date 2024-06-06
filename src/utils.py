"""Модуль для работы с JSON файлами"""

import json


def get_data_from_json_file(path: str) -> list[dict]:
    """Функция принимает путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях."""
    try:
        with open(path) as file:
            try:
                operations = json.load(file)
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []
    if not type(operations) is list:
        return []

    return operations
