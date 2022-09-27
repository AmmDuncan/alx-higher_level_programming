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
        if type(attrs) == list\
                and len(attrs) > 0 \
                and all(type(s) == str for s in attrs):
            new_dict = {}
            for key in self.__dict__:
                if key in attrs:
                    new_dict[key] = self.__dict__[key]
            return new_dict
        return self.__dict__
