"""
File I/O Assignment
"""

import calendar


def get_days_in_month(year, month):
    """Get the number of days in a given month of a given year."""
    return calendar.monthrange(year, month)[1]
