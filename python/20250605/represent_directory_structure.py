"""
This module provides a function to
build a directory structure
"""

import os


def get_directory_structure(path):
    """
    Recursively builds a dictionary
    representing the structure of a directory.
    """
    structure = {"name": os.path.basename(path), "type": "directory", "children": []}

    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            structure["children"].append(get_directory_structure(full_path))
        else:
            structure["children"].append({"name": item, "type": "file"})

    return structure
