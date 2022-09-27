#!/usr/bin/python3
"""Define MyList that extends list class"""


class MyList(list):
    """Extension of list class"""

    def print_sorted(self):
        """Print sorted list of ints"""
        sorted_list = sorted(self)
        print(sorted_list)
