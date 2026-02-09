#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    with open("my_obj.json", "w") as filename:
        json.dump(my_obj, filename)
        