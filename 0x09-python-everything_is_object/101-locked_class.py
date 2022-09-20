#!/usr/bin/python3
"""Module to define LockedClass"""


class LockedClass():
    def __init__(self,):
        self.first_name = None

    def __setattr__(self, __name, __value):
        if (__name == "__dict__"):
            return False
        self.__dict__ = {"first_name": self.__dict__.get("first_name")}


n = LockedClass()
n.last_name = "Snow"

print(n.__dict__)
