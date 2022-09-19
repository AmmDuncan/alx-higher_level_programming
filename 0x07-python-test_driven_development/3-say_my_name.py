#!/usr/bin/python3
"""3-say_my_name module"""


def say_my_name(first_name, last_name=""):
    """Print my name"""
    is_string(first_name, "first_name")
    is_string(last_name, "last_name")
    message = "My name is {} {}"
    print(message.format(first_name, last_name))


def is_string(v, name=""):
    """Check if value is string"""
    if type(v) != str:
        raise TypeError("{} must be a string".format(name))
