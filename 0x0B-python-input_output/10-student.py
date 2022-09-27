#!/usr/bin/python3
"""Student to JSON"""


class Student():
    """Represents Student class"""

    def __init__(self, first_name, last_name, age):
        """Instantiate Student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Convert Student object to json object"""
        if type(attrs) is list\
                and len(attrs) > 0 and type(attrs[0]) is str:
            new_dict = {}
            for key, value in self.__dict__:
                if key in attrs:
                    new_dict[key] = value
            return new_dict
        return self.__dict__
