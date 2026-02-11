#!/usr/bin/python3
"""
This module provides a function that converts a JSON string
into its corresponding Python object.
"""

import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure)
    represented by a JSON string
    """

    # Convert the JSON string into a Python data structure
    return json.loads(my_str)
