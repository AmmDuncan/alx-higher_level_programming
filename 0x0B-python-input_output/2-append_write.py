#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """append text to end of file"""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
    return len(text)
