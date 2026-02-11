#!/usr/bin/python3
"""
This module provides a function that saves a Python object
to a file in JSON format.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file using JSON representation.

    Args:
        my_obj: The Python object to save.
        filename (str): The name of the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
        