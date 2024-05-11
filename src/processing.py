"""Модуль фильтрации и сортировки операций"""


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
