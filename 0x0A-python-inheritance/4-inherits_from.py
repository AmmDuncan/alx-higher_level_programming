#!/usr/bin/python3
"""Check if object is instance of a class that inherits
    directly or indirectly from the specified calss"""


def inherits_from(obj, a_class):
    """Check if obj is instance of a class that inherits
        from a_class"""
    return issubclass(obj.__class__, a_class) \
        and obj.__class__ is not a_class
