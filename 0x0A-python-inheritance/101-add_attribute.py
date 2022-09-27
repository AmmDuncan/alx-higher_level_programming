#!/usr/bin/python3
"""Can I?"""


def add_attribute(obj, key, value):
    """add attr to object if possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)
