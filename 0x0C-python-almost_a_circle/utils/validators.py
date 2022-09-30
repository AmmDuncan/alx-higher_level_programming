#!/usr/bin/python3
"""Validation utility functions"""


def is_integer(value, name="value"):
    """Check if value is integer"""
    if type(value) != int:
        raise TypeError("{} must be an integer".format(name))


def is_positive_integer(value, name="value"):
    """Check if value if a positive integer"""
    is_integer(value, name)
    if value <= 0:
        raise ValueError("{} must be > 0".format(name))


def is_non_negative_integer(value, name="value"):
    """Check if value is a non negative integer"""
    is_integer(value, name)
    if value < 0:
        raise ValueError("{} must be >= 0".format(name))
