"""Task 6: Add quantity and revenue columns to the daily prices data."""

import os
import numpy as np
import pandas as pd


def add_quantity_and_revenue(
    input_path="daily_prices.csv", output_path="daily_revenues.csv"
):
    """Add quantity and revenue columns to the daily prices data."""
    try:
        df = pd.read_csv(input_path)
        df["quantity"] = np.round(np.random.uniform(10, 100, size=len(df)), 2)
        df["revenue"] = df["price"] * df["quantity"]
        if not os.path.exists(output_path):
            df.to_csv(output_path, index=False)
        else:
            print(f"{output_path} already exists.")
    except FileNotFoundError:
        print(f"Input file not found: {input_path}")
