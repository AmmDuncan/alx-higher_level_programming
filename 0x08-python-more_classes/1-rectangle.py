#!/usr/bin/python3
"""
The "1-rectangle" module
========================
Defines read definition of Rectangle class
"""


class Rectangle():
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialize new Rectangle"""
        validate_length(width, "width")
        validate_length(height, "height")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        validate_length(value, "width")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        validate_length(value, "height")
        self.__height = value


def validate_length(value, name):
    """Check if value is an int and is not negative

    Args:
        value (any): value to validate
        name (str): name to use in error message
    """
    is_int(value, name)
    is_not_negative(value, name)


def is_int(val, name="value"):
    """Check if value is integer

    Args:
        val (any): value to perform type check on 
        name (str, optional): name to use in case of type error. Defaults to "value".

    Raises:
        TypeError: if val is not an integer
    """
    if type(val) != int:
        raise TypeError("{} must be an integer".format(name))


def is_not_negative(val, name="value"):
    """Check if value is not negative

    Args:
        val (int): value to perform check on
        name (str, optional): name to use in error message. Defaults to "value".

    Raises:
        ValueError: if value is negative
    """
    if val < 0:
        raise ValueError("{} must be >= 0".format(name))
