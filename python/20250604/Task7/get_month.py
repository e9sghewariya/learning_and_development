"""File I/O Assignment"""
from datetime import datetime

def get_month(date_str):
    """Extract the month from a date string in YYYY/MM/DD format."""
    try:
        dt = datetime.strptime(date_str, "%Y/%m/%d")
        return dt.month
    except ValueError:
        print("Invalid date format.")
        return None
