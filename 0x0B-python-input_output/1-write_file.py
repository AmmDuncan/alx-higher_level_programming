#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """Write text to file: filename"""
    with open(filename, "w", encoding="utf-8") as a_file:
        a_file.write(text)
    return len(text)
