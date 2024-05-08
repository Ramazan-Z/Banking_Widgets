from src.processing import filter_state_operations, sorted_date_operacions
from src.widget import format_date, format_requesite

if __name__ == "__main__":
    card = "Visa Platinum 8990922113665229"
    account = "Счет 73654108430135874305"
    date = "2018-07-11T02:26:18.671407"

    print(format_requesite(card))
    print(format_requesite(account))
    print(format_date(date), "\n")

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
