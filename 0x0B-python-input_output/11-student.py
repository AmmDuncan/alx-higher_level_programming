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
        if (type(attrs) == list and
                all(type(s) == str for s in attrs)):
            new_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    new_dict[key] = self.__dict__[key]
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Reload object from json"""
        self.__dict__ = json
