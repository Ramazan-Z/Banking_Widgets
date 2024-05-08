from src.widget import format_date, format_requesite

if __name__ == "__main__":
    card = "Visa Platinum 8990922113665229"
    account = "Счет 73654108430135874305"
    date = "2018-07-11T02:26:18.671407"

    print(format_requesite(card))
    print(format_requesite(account))
    print(format_date(date))
