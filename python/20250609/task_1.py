"""tas1k_1.py script"""

import pandas as pd

# Load datasets
dam = pd.read_csv("DAM_Prices_2022.csv")
rtm = pd.read_csv("RTM_Prices_2022.csv")

# Filter for HB_NORTH
dam = dam[dam["Settlement Point"] == "HB_NORTH"]
rtm = rtm[rtm["Settlement Point"] == "HB_NORTH"]

# Create datetime column (hour start) for both
dam["date"] = pd.to_datetime(dam["Delivery Date"], format="%m/%d/%Y") + pd.to_timedelta(
    dam["Delivery Hour"] - 1, unit="h"
)
rtm["date"] = (
    pd.to_datetime(rtm["Delivery Date"], format="%m/%d/%Y")
    + pd.to_timedelta(rtm["Delivery Hour"] - 1, unit="h")
    + pd.to_timedelta((rtm["Delivery Interval"] - 1) * 15, unit="min")
)

# DAM: Keep only date and price columns, rename columns
dam_hourly = dam[["date", "Settlement Point Price"]].rename(
    columns={"Settlement Point Price": "dam"}
)

# RTM: Resample to hourly and take mean
rtm.set_index("date", inplace=True)
rtm_hourly = (
    rtm["Settlement Point Price"]
    .resample("H")
    .mean()
    .reset_index()
    .rename(columns={"Settlement Point Price": "rtm"})
)

# Merge on datetime
merged_data = pd.merge(dam_hourly, rtm_hourly, on="date")

# Round to 2 decimal places
merged_data["dam"] = merged_data["dam"].round(2)
merged_data["rtm"] = merged_data["rtm"].round(2)

# Save to CSV
merged_data.to_csv("task_1.csv", index=False)
