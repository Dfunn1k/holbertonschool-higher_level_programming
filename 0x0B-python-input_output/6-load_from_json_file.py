#!/usr/bin/python3
"""Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """Function that creates an Object from a “JSON file”"""
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
    return json.loads(read_data)
