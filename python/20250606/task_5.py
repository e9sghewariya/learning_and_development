"""Task 5: Generate a daily price dataset for commodities."""

import random
import os
import pandas as pd


def generate_price_data(output_path="daily_prices.csv"):
    """Generate a daily price dataset for commodities."""
    dates = pd.date_range(start="2023-07-19", end="2025-05-27", freq="D")
    commodities = ["White Gold", "Silver", "Platinum", "Rose Gold"]

    dfs = []
    for commodity in commodities:
        prices = [round(random.uniform(40, 100), 2) for _ in range(len(dates))]
        df = pd.DataFrame({"date": dates, "commodity": commodity, "price": prices})
        dfs.append(df)

    full_df = pd.concat(dfs, ignore_index=True)
    if not os.path.exists(output_path):
        full_df.to_csv(output_path, index=False)
    else:
        print(f"{output_path} already exists.")
