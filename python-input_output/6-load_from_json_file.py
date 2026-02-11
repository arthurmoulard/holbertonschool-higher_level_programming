#!/usr/bin/python3
"""
This module provides a function that creates a Python object
from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file
    """

    # Open the file in read mode using 'with'
    with open(filename, "r", encoding="utf-8") as f:
        # Load and return the Python object from the JSON file
        return json.load(f)
    