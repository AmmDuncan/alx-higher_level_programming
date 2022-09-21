#!/usr/bin/python3
"""
module that defines text_indentation function
"""


def text_indentation(text):
    """prints test with 2 new lines after '.', '?', and ':'"""
    if type(text) != str:
        raise TypeError("text must be a string")

    new_str = ""
    chunks = []
    keychars = ['.', '?', ':']
    text_len = len(text)
    for char_i in range(text_len):
        char = text[char_i]
        if char in keychars:
            new_str += char
            chunks.append(new_str)
            new_str = ""
        else:
            new_str += char
    if new_str:
        chunks.append(new_str)
    chunks = [*map(lambda c: c.strip(), chunks)]
    new_str = "\n\n".join(chunks)
    end = "\n\n" if text[text_len - 1] in keychars else ""
    print(new_str, end=end)
