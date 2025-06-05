"""File I/O Assignment"""
from ...get_month import get_month
from ...get_no_of_days import get_days_in_month


def display_days():
    """
    Display the number of days in a month based on user input.
    """
    date_str = input("Enter date (YYYY/MM/DD): ")
    parts = date_str.split("/")
    if len(parts) == 3:
        year = int(parts[0])
        month = get_month(date_str)
        if month:
            days = get_days_in_month(year, month)
            print(f"Days in month: {days}")
    else:
        print("Invalid input format.")


display_days()
