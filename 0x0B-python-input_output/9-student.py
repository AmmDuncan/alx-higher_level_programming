#!/usr/bin/python3
"""Student to JSON"""


class Student():
    """Represents Student class"""

    def __init__(self, first_name, last_name, age):
        """Instantiate Student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Convert Student object to json object"""
        return self.__dict__
