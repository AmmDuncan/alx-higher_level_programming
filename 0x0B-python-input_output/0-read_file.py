#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """read file and write content to stdout"""
    content = ""
    with open(filename, encoding="utf-8") as a_file:
        content = a_file.read()
        print(content, end="")
