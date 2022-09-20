#!/usr/bin/python3
"""
4-print_square module
=====================
module that defines the print_square function
"""


def print_square(size):
    """Print square made of #"""
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()
