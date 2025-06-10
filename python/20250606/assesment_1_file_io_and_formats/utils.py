"""Utility module for file format conversion with sample data support."""

import os
import json
import random
import pandas as pd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def _generate_sample_json_data(json_path, num_records=13):
    """
    Generate a sample JSON file with random data.
    """

    names = [
        "Sheldon",
        "Leonard",
        "Penny",
        "Raj",
        "Howard",
        "Amy",
        "Bernadette",
        "Stuart",
        "Joey",
        "Chandler",
        "Ross",
        "Monica",
        "Rachel",
    ]

    data = []

    for _ in range(num_records):
        entry = {
            "id": random.randint(1000, 9999),
            "name": random.choice(names),
            "age": random.randint(20, 50),
            "score": round(random.uniform(0, 100), 2),
        }
        data.append(entry)

    with open(json_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def _generate_sample_csv_data(csv_path, num_records=13):
    """
    Generate a sample CSV file with random data.
    """

    names = [
        "Naruto",
        "Sasuke",
        "Sakura",
        "Kakashi",
        "Hinata",
        "Shikamaru",
        "Kirito",
        "Asuna",
        "Leafa",
        "Sinon",
        "Klein",
        "Agil",
    ]
    data = []

    for _ in range(num_records):
        data.append(
            {
                "id": random.randint(1000, 9999),
                "name": random.choice(names),
                "age": random.randint(20, 50),
                "score": round(random.uniform(0, 100), 2),
            }
        )

    df = pd.DataFrame(data)
    df.to_csv(csv_path, index=False, encoding="utf-8")


def json_to_csv(json_path):
    """
    Convert a JSON file to a CSV file.
    If the JSON file does not exist, generate sample data.
    """

    if not os.path.exists(json_path):
        _generate_sample_json_data(json_path)

    csv_path = os.path.splitext(json_path)[0] + ".csv"
    if os.path.exists(csv_path):
        raise FileExistsError(f"File already exists: {csv_path}")

    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    df1 = pd.DataFrame(data)
    df1.to_csv(csv_path, index=False)

    return csv_path


def csv_to_json(csv_path):
    """
    Convert a CSV file to a JSON file.
    If the CSV file does not exist, generate sample data.
    """
    if not os.path.exists(csv_path):
        _generate_sample_csv_data(csv_path)

    json_path = os.path.splitext(csv_path)[0] + ".json"

    if os.path.exists(json_path):
        raise FileExistsError(f"File already exists: {json_path}")

    df2 = pd.read_csv(csv_path)
    df2.to_json(json_path, orient="records", indent=4)
    return json_path


if __name__ == "__main__":
    json_input_path = os.path.join(SCRIPT_DIR, "sample_data.json")
    csv_file = json_to_csv(json_input_path)
    print(f"Generated CSV: {csv_file}")

    csv_input_path = os.path.join(SCRIPT_DIR, "sample_data.csv")
    json_file = csv_to_json(csv_input_path)
    print(f"Generated JSON: {json_file}")
