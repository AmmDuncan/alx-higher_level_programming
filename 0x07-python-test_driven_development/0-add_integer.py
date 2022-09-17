#!/usr/bin/python3
"""
    module that defines add_integer function that sums
    two integers
"""

def add_integer(a, b=98):
    """function to add two integers; a and b"""
    is_int_or_float(a, "a")
    is_int_or_float(b, "b")

    return int(a) + int(b)

def is_int_or_float(v, name):
    """function to check if value is int or float"""
    if type(v) not in [int, float]:
        raise TypeError("{} must be an integer".format(name))
