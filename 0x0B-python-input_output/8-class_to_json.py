#!/usr/bin/python3
"""Class to JSON"""
import json


def class_to_json(obj):
    """Convert class obj to json string"""
    return json.dumps(obj.__dict__)
