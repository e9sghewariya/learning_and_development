"""Task 2: Process DAM and RTM prices for HB_NORTH"""

import pandas as pd

# Load datasets
dam = pd.read_csv("DAM_prices_2022.csv")
rtm = pd.read_csv("RTM_prices_2022.csv")

# Filter for HB_NORTH
dam = dam[dam["Settlement Point"] == "HB_NORTH"]
rtm = rtm[rtm["Settlement Point"] == "HB_NORTH"]

# Create datetime column for DAM (hourly)
dam["date"] = pd.to_datetime(dam["Delivery Date"], format="%m/%d/%Y") + pd.to_timedelta(
    dam["Delivery Hour"] - 1, unit="h"
)
dam = dam[["date", "Settlement Point Price"]].rename(
    columns={"Settlement Point Price": "dam"}
)
dam.set_index("date", inplace=True)

# Create 15-min datetime range and reindex DAM with ffill
full_15min_index = pd.date_range(
    start="2022-01-01 00:00:00", end="2022-01-31 23:45:00", freq="15min"
)
dam_15min = (
    dam.reindex(full_15min_index)
    .ffill()
    .reset_index()
    .rename(columns={"index": "date"})
)

# Create datetime column for RTM (15-min)
rtm["date"] = (
    pd.to_datetime(rtm["Delivery Date"], format="%m/%d/%Y")
    + pd.to_timedelta(rtm["Delivery Hour"] - 1, unit="h")
    + pd.to_timedelta((rtm["Delivery Interval"] - 1) * 15, unit="min")
)
rtm = rtm[["date", "Settlement Point Price"]].rename(
    columns={"Settlement Point Price": "rtm"}
)

# Merge DAM and RTM on 15-min datetime
merged_15min = pd.merge(dam_15min, rtm, on="date")

# Round to 2 decimal places
merged_15min["dam"] = merged_15min["dam"].round(2)
merged_15min["rtm"] = merged_15min["rtm"].round(2)

# Save to CSV
merged_15min.to_csv("task_2.csv", index=False)
