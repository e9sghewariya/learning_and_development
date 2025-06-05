"""
This module has a function that recursively searches for a specific 
file name in a given directory and all its subdirectories.
Return the full path of the file if found
"""
import os

def search_file_recursively(start_path, target_filename):
    """
    Searches for a file with the specified name in the directory tree
    starting from the given path.
    """
    for root, _, files in os.walk(start_path):
        if target_filename in files:
            return os.path.join(root, target_filename)
    return None
