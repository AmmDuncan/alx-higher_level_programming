#!/usr/bin/python3
"""Base module"""
import json
from operator import truediv


class Base():
    """Represents a Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiate a Base class"""
        if id is not None:
            self.id = id
        else:
            Base. __nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries=None):
        """Convert list of dicts to json"""
        if list_dictionaries is None:
            return '"[]"'
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string=None):
        """Convert json string to list of dicts"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs=None):
        """Save list of objects to file"""
        with open(f"{cls.__name__}.json", "w") as file:
            if list_objs is None:
                file.write('"[]"')
            else:
                dict_list = [*map(lambda obj: obj.to_dictionary(), list_objs)]
                json_s = Base.to_json_string(dict_list)
                file.write(json_s)

    @classmethod
    def load_from_file(cls):
        """Save list of objects to file"""
        with open(f"{cls.__name__}.json", "r") as file:
            list_of_obj = Base.from_json_string(file.read())
            dict_list = [*map(lambda obj: cls.create(**obj), list_of_obj)]
            return dict_list

    @classmethod
    def create(cls, **dictionary):
        """Create instance object"""
        obj = cls(1, 1, 0, 0)
        obj.update(**dictionary)
        return obj

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save objects to csv file"""
        cls_name = cls.__name__
        with open(f"{cls_name}.csv", "w") as file:
            if cls_name == 'Rectangle':
                file.write('id, width, height, x, y\n')
                for obj in list_objs:
                    file.write(
                        f"{obj.id}, {obj.width}, {obj.height}, {obj.x}, {obj.y}\n")
            elif cls_name == "Square":
                file.write('id, size, x, y\n')
                for obj in list_objs:
                    file.write(
                        f"{obj.id}, {obj.size}, {obj.x}, {obj.y}\n")

    @classmethod
    def load_from_file_csv(cls):
        """Load objects to csv file"""
        cls_name = cls.__name__
        res_list = []
        with open(f"{cls_name}.csv", "r") as file:
            if cls_name == 'Rectangle':
                lines = file.readlines()
                for line in lines[1:]:
                    args = line.rstrip().split(', ')
                    args = [*map(lambda x: int(x.strip()), args)]
                    kwargs = dict(
                        zip('id, width, height, x, y'.split(', '), args))
                    res_list.append(cls.create(**kwargs))

            elif cls_name == "Square":
                lines = file.readlines()
                for line in lines[1:]:
                    args = line.rstrip().split(', ')
                    args = [*map(lambda x: int(x.strip()), args)]
                    kwargs = dict(
                        zip('id, size, x, y'.split(', '), args))
                    res_list.append(cls.create(**kwargs))
        return res_list
