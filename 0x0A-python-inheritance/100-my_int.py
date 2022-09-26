#!/usr/bin/python3
"""Extend int class"""


class MyInt(int):
    """Custom integer class"""

    def __eq__(self, to):
        """inverted equal"""
        return super().__ne__(to)

    def __ne__(self, to):
        """inverted not equal"""
        return super().__eq__(to)
