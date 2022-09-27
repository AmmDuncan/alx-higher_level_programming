#!/usr/bin/python3
"""List all available attributes and methods
    of an object"""


def lookup(obj):
    """Return list of available attrs and methods on obj"""
    return dir(obj)
