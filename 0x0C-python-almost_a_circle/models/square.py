#!/usr/bin/python3
"""Define Square class"""
from models.rectangle import Rectangle
from utils.validators import is_non_negative_integer, is_positive_integer


class Square(Rectangle):
    """Representation of Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square object"""
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """Update Square object"""
        if args and len(args):
            nones = [None] * 4
            for i in range(4):
                if i < len(args):
                    nones[i] = args[i]
            id, size, x, y = nones
        else:
            id = kwargs.setdefault('id', None)
            size = kwargs.setdefault('size', None)
            x = kwargs.setdefault('x', None)
            y = kwargs.setdefault('y', None)
        if id:
            self.id = id
        if size:
            is_positive_integer(size, "size")
            self.width = size
            self.height = size
        if x:
            is_non_negative_integer(x, "x")
            self.x = x
        if y:
            is_non_negative_integer(y, "y")
            self.y = y

    @property
    def size(self):
        """Getter for size property"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size property"""
        is_positive_integer(value, "size")
        self.width = value
        self.height = value

    def to_dictionary(self):
        """Get square instance properties as dict"""
        rect_dict = {}
        rect_dict['id'] = self.id
        rect_dict['size'] = self.width
        rect_dict['x'] = self.x
        rect_dict['y'] = self.y
        return rect_dict

    def __str__(self):
        """String representation of square object"""
        return ("[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.size,
        ))
