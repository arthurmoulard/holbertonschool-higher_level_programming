#!/usr/bin/python3
"""
This script adds all command-line arguments to a JSON file (add_item.json).
It loads the existing list from the file, appends new arguments, and saves
the updated list back. The JSON file is created if it does not exist.
"""

import sys
# Import path to check if a file exists
from os import path
# Import functions from previous tasks using dynamic import
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


"""
Main function to add command-line arguments to a JSON file.
"""
# Retrieve the list of command line arguments
args = sys.argv

# Check if the JSON file already exists
if path.exists('add_item.json'):
    # Load the existing list from the JSON file
    list = load_from_json_file('add_item.json')
else:
    # If the file does not exist, initialize an empty list
    list = []

# Save the list to the JSON file (creates the file if needed)
save_to_json_file(list, 'add_item.json')

# If there are additional command line arguments
if len(sys.argv) >= 2:
    # Append each argument (except the script name) to the list
    for i in range(1, len(sys.argv)):
        list.append(sys.argv[i])

# Save the updated list back to the JSON file
save_to_json_file(list, 'add_item.json')
