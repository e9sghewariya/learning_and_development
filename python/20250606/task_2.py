"""Script for assignment 2"""

import pandas as pd


# Demonstrate the difference between
# .loc and .iloc using
# suitable examples
def demonstrate_loc_iloc():
    """Demonstrate the difference between .loc and .iloc."""
    df = pd.DataFrame({"A": list("abc"), "B": [1, 2, 3]}, index=[101, 102, 103])

    print("Using .loc (label-based):")
    print(df.loc[101])

    print("\nUsing .iloc (position-based):")
    print(df.iloc[0])


demonstrate_loc_iloc()
