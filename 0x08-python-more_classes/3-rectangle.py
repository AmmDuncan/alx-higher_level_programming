#!/usr/bin/python3
"""Module to define Rectangle class with area and perimeter methods"""


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

    def area(self):
        """Calculate area of rectangle

        Returns:
            int: height x width
        """
        return self.__height * self.__width

    def perimeter(self):
        """Calculate perimeter of rectangle

        Returns:
            int: (2 x height) + (2 x width)
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        new_str = ""
        if self.__width == 0 or self.__height == 0:
            return new_str
        for i in range(self.__height):
            end_char = "\n" if i != self.__height - 1 else ""
            row = ("#" * self.__width) + end_char
            new_str += row
        return new_str


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
        name (str, optional): name to use in case of
            type error. Defaults to "value".

    Raises:
        TypeError: if val is not an integer
    """
    if type(val) != int:
        raise TypeError("{} must be an integer".format(name))


def is_not_negative(val, name="value"):
    """Check if value is not negative

    Args:
        val (int): value to perform check on
        name (str, optional): name to use in error message.
            Defaults to "value".

    Raises:
        ValueError: if value is negative
    """
    if val < 0:
        raise ValueError("{} must be >= 0".format(name))
