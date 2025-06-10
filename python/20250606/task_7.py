"""Task 7: Revenue analysis from daily_revenues.csv

This script analyzes daily revenues from a CSV file.
It calculates the average price of Silver in 2024,
total revenue for White Gold and Rose Gold between specified dates,
and identifies months with revenue greater than the overall monthly average.
"""

import pandas as pd


def analyze_revenues(path="daily_revenues.csv"):
    """Perform 3 revenue analysis subtasks
    using daily_revenues.csv."""
    try:
        # Read the CSV with date parsing
        df = pd.read_csv(path, parse_dates=["date"])

        # --- 7.1 Average price for Silver in 2024 ---
        silver_2024 = df[(df["commodity"] == "Silver") & (df["date"].dt.year == 2024)]
        avg_price_silver_2024 = silver_2024["price"].mean()
        print(f"7.1 Average Silver Price in 2024: {avg_price_silver_2024:.2f}")

        # --- 7.2 Total revenue for White Gold & Rose Gold between dates ---
        date_filter = (df["date"] >= "2023-12-01") & (df["date"] <= "2024-11-30")
        golds = df[date_filter & df["commodity"].isin(["White Gold", "Rose Gold"])]
        total_revenue = golds["revenue"].sum()
        print(f"7.2 Total Revenue (White Gold + Rose Gold): {total_revenue:.2f}")

        # --- 7.3 Months with revenue > overall monthly average ---
        df["month"] = df["date"].dt.to_period("M")
        monthly_avg_revenue = []

        for month in df["month"].unique():
            month_df = df[df["month"] == month]
            avg = month_df["revenue"].mean()
            monthly_avg_revenue.append((str(month), avg))

        overall_avg = df["revenue"].mean()
        print(f"Overall Monthly Avg Revenue: {overall_avg:.2f}")

        print("7.3 Months where revenue > overall average:")
        for month, avg in monthly_avg_revenue:
            if avg > overall_avg:
                print(f"{month}: {avg:.2f}")

    except FileNotFoundError:
        print(f"File not found: {path}")
    except (KeyError, ValueError, pd.errors.ParserError) as e:
        print(f"Error while processing data: {e}")


if __name__ == "__main__":
    analyze_revenues()
