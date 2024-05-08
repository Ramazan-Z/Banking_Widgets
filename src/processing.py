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


if __name__ == "__main__":
    test_operations = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    print(filter_state_operations(test_operations), "\n")
    print(filter_state_operations(test_operations, "CANCELED"), "\n")

    print(sorted_date_operacions(test_operations), "\n")
    print(sorted_date_operacions(test_operations, decreasing=False))
