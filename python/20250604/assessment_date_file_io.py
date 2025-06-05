"""
assessment_date_file_io.py
This script contains various tasks 
related to date and file operations in Python.
"""

import os
import json
import datetime
import shutil
from datetime import timedelta



# #Task1: Age Calculator - python
#     1. Take `Date of Birth`(str - %Y-%m-%d) as an input from user.
#     2. Calculate and display the current age based on `Date of Birth`.
from datetime import datetime


def age_calculator():
    """Calculate and display the user's age based on their date of birth."""
    while True:
        dob_str = input("Enter your date of birth (YYYY-MM-DD): ")
        try:
            dob = datetime.strptime(dob_str, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid format. Please use YYYY-MM-DD.")

    today = datetime.today()
    age = today.year - dob.year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    print(f"You are {age} years old.")


age_calculator()


# - Task2: Dates in different timezones - python
#     1. Take a list of timezones as an input from the user.
#     2. Display current time in each of those timezones.

def show_time_in_timezones():
    """Display current time in different timezones based on user input."""
    user_input = input("Enter comma-separated UTC offsets (e.g., +5.5, -4, 0): ")
    offsets = user_input.split(",")

    for offset_str in offsets:
        try:
            offset = float(offset_str.strip())
            now_utc = datetime.now()
            local_time = now_utc + timedelta(hours=offset)
            print(f"UTC{offset:+}: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")
        except ValueError:
            print(f"Invalid offset: {offset_str}")


show_time_in_timezones()

# Task3: File organization - python
# 1. Take a directory path as an input from user.
# 2. Based on the filetype(file extension),
# organize the files in different subdirectories.
# 3. Print structure of this directory.


def organize_files_by_type(directory):
    """Organize files in a directory by their file extensions."""
    if not os.path.isdir(directory):
        print("Invalid directory.")
        return

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            ext = filename.split(".")[-1] if "." in filename else "no_extension"
            dest_dir = os.path.join(directory, ext)
            if not os.path.exists(dest_dir):
                os.mkdir(dest_dir)
            shutil.move(filepath, os.path.join(dest_dir, filename))

    print("Files organized by extension.")


# - Task6: Combine and store json
#     1. Combine the data from all the files in test_data.
#     2. Store it in a file named "combined_data.json"
#     3. Sort the data in this file based on the key "name".
#     4. Store the sorted results in file "sorted_data.json"


def combine_and_sort_json(folder):
    """Combine JSON files in a folder and sort the data by 'name'."""
    combined_data = []

    for filename in os.listdir(folder):
        if filename.endswith(".json"):
            with open(os.path.join(folder, filename), "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    combined_data.extend(data)
                else:
                    combined_data.append(data)

    with open("combined_data.json", "w", encoding="utf-8") as f:
        json.dump(combined_data, f, indent=2)

    sorted_data = sorted(combined_data, key=lambda x: x.get("name", ""))
    with open("sorted_data.json", "w", encoding="utf-8") as f:
        json.dump(sorted_data, f, indent=2)
