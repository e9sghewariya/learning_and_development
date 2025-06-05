"""This module takes two json files
and merges them into one
also manages conflicts
when the same key exists in both files.
"""

import json


def merge_json_with_conflict_handling(json_files, output_file):
    """Merges multiple JSON files into one,
    handling conflicts by combining values.
    """
    merged_data = {}

    for file in json_files:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

        for key, value in data.items():
            if key not in merged_data:
                merged_data[key] = value
            else:
                if not isinstance(merged_data[key], list):
                    merged_data[key] = [merged_data[key]]
                merged_data[key].append(value)

    with open(output_file, "w", encoding="utf-8") as out:
        json.dump(merged_data, out, indent=4)
