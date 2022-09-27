#!/usr/bin/python3
"""Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """Load object from JSON file"""
    with open(filename, "r", encoding="utf-8") as file:
        content = json.loads(file.read())
    return content
