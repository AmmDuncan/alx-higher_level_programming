#!/usr/bin/python3
"""BaseGeometry with area method"""


class BaseGeometry():
    """BaseGeometry class without area implementation"""

    def area(self):
        """Unimplemented method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate integer"""
        is_integer(value, name)
        is_positive(value, name)


def is_integer(value, name):
    """Validate if value is integer"""
    if type(value) != int:
        raise TypeError("{} must be an integer".format(name))


def is_positive(value, name):
    """Validate if value is greater than 0"""
    if type(value) == int and value <= 0:
        raise ValueError("{} must be greater than 0".format(name))
