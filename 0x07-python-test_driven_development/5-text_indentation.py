#!/usr/bin/python3
"""
module that defines text_indentation function
"""


def text_indentation(text):
    """prints test with 2 new lines after '.', '?', and ':'"""
    if type(text) != str:
        raise TypeError("text must be a string")

    keychars = ['.', '?', ':']
    text_len = len(text)
    for char_i in range(text_len):
        char = text[char_i]
        not_first = char_i != 0
        is_space_to_remove = char == " " and text[char_i - 1] in keychars
        whitespace = not_first and is_space_to_remove
        if not whitespace:
            print(char, end="")
        if char in keychars:
            print("\n")
