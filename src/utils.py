"""Модуль для работы с JSON файлами"""

import json
import logging
import os

# Создание логера
logg = logging.getLogger(__name__)
# Создание хендлера
file_handler = logging.FileHandler(os.path.join("logs", "get_data_from_json_file.log"), "w")
# Создание форматера
file_formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s: %(message)s")
# Установка форматера
file_handler.setFormatter(file_formatter)
# Добавление хендлера к логеру
logg.addHandler(file_handler)
# Настройка уровня логирования
logg.setLevel(logging.DEBUG)


def get_data_from_json_file(path: str) -> list[dict]:
    """Функция принимает путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях."""
    try:
        logg.info("Попытка открытия файла")
        with open(path) as file:
            logg.info("Файл открыт")
            try:
                logg.info("Начало загрузки файла")
                operations = json.load(file)
                logg.info("Загрузка файла завершена")
            except json.JSONDecodeError:
                logg.error("Ошибка загрузки файла")
                logg.error("Завершение программы, транзакций не найдено")
                return []
    except FileNotFoundError:
        logg.error("Ошибка открытия файла")
        logg.error("Завершение программы, транзакций не найдено")
        return []
    if not type(operations) is list:
        logg.error("Файл не содержит транзакций")
        logg.error("Завершение программы, транзакций не найдено")
        return []

    logg.info("Успешное завершение программы")
    return operations
