"""3. Read a CSV file, specifying column data
# types explicitly and not relying on
# pandas' inference"""

from numpy import int64
import pandas as pd


def read_csv_with_dtypes(path):
    """Read a CSV file with explicit dtypes."""
    try:
        dtypes = {"name": str, "id": int64, "score": float}
        df = pd.read_csv(path, dtype=dtypes)
        print(df.dtypes)
    except FileNotFoundError:
        print("File not found.")


read_csv_with_dtypes("sample_data.csv")
