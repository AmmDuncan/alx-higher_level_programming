#!/usr/bin/python3
"""Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """Find an insert newstring where search string occurs"""
    with open(filename, "r", encoding="utf-8") as file:
        lines = []
        for line in file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(lines)
