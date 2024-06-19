"""Модуль фильтрации и сортировки операций"""

import re
from collections import Counter

from src.generators import transaction_descriptions


def filter_state_operations(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция принимает список словарей и ключ состояния (по умолчанию EXECUTED),
    возвращает список словарей с принятым ключoм состояния"""
    list_to_return = []

    for operation in operations:
        if operation.get("state") == state:
            list_to_return.append(operation)

    return list_to_return


def sorted_date_operacions(operations: list[dict], decreasing: bool = True) -> list[dict]:
    """Функцию принимает список словарей и возвращает новый список,
    в котором исходные словари отсортированы по убыванию
    (опционально по возрастанию) даты"""

    return sorted(operations, key=lambda x: x["date"], reverse=decreasing)


def filter_by_line_in_description(operations: list[dict], search_string: str) -> list[dict]:
    """Функция принимает список словарей с транзакциями и строку поиска.
    Возвращает список словарей, у которых в описании есть данная строка."""
    search_results_list = []
    for operation in operations:
        if re.search(search_string, operation["description"], flags=re.IGNORECASE):
            search_results_list.append(operation)

    return search_results_list


def count_transactions_by_category(transactions: list[dict], categories: list[str]) -> dict:
    """Функция принимает список словарей с данными о банковских операциях
    и список категорий операций, а возвращает словарь, в котором ключи — это
    названия категорий, а значения — это количество операций в каждой категории"""
    count_list = [x for x in transaction_descriptions(transactions) if x in categories]
    return dict(Counter(count_list))
