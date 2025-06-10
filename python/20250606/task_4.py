"""Task 4: Extract specific columns from a CSV file."""

import pandas as pd


def print_nth_column(path, n):
    """Print nth column of a CSV file."""
    try:
        df = pd.read_csv(path)
        if n < 0 or n >= len(df.columns):
            print("Invalid column index.")
            return
        print(df.iloc[:, n])
    except FileNotFoundError:
        print(f"File not found: {path}")
    except pd.errors.EmptyDataError:
        print("CSV file is empty.")
    except pd.errors.ParserError:
        print("Error parsing the CSV file.")


def print_column_by_name(path, column_name):
    """Print column by name."""
    try:
        df = pd.read_csv(path)
        if column_name not in df.columns:
            print("Column not found.")
            return
        print(df[column_name])
    except FileNotFoundError:
        print(f"File not found: {path}")
    except pd.errors.EmptyDataError:
        print("CSV file is empty.")
    except pd.errors.ParserError:
        print("Error parsing the CSV file.")
