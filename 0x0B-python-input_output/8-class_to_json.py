#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    """Convert class obj to json object"""
    return obj.__dict__
