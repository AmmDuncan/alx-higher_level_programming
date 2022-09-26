#!/usr/bin/python3
"""Check if obj is exactly and instance of a class"""

def is_same_class(obj, a_class):
    """Check is obj is an exact instance of a_class"""
    return obj.__class__ == a_class

