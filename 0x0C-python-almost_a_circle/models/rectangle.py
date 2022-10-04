#!/usr/bin/python3
"""Define Rectangle class"""
from models.base import Base
from utils.validators import is_positive_integer, is_non_negative_integer


class Rectangle(Base):
    """Representation of Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiate Rectangle object"""
        super().__init__(id)
        is_positive_integer(width, "width")
        is_positive_integer(height, "height")
        is_non_negative_integer(x, "x")
        is_non_negative_integer(y, "y")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute"""
        is_positive_integer(value, "width")
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute"""
        is_positive_integer(value, "height")
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x attribute"""
        is_non_negative_integer(value, "x")
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y attribute"""
        is_non_negative_integer(value, "y")
        self.__y = value

    def update(self, *args, **kwargs):
        """Update Rectangle object"""
        if args and len(args):
            nones = [None] * 5
            for i in range(5):
                if i < len(args):
                    nones[i] = args[i]
            id, width, height, x, y = nones
        else:
            id = kwargs.setdefault('id', None)
            width = kwargs.setdefault('width', None)
            height = kwargs.setdefault('height', None)
            x = kwargs.setdefault('x', None)
            y = kwargs.setdefault('y', None)
        if id:
            self.id = id
        if width:
            is_positive_integer(width, "width")
            self.__width = width
        if height:
            is_positive_integer(height, "height")
            self.__height = height
        if x:
            is_non_negative_integer(x, "x")
            self.__x = x
        if y:
            is_non_negative_integer(y, "y")
            self.__y = y

    def area(self):
        """Calculate area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """Display rectangle in stdout"""
        h = self.__height
        w = self.__width
        for _ in range(self.__y):
            print()
        for _ in range(h):
            for _ in range(self.__x):
                print(" ", end="")
            print("#" * w)

    def __str__(self):
        """String representation of rectangle"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.__x,
            self.__y,
            self.__width,
            self.__height
        ))

    def to_dictionary(self):
        """Get dictionary properties as dictionary"""
        rect_dict = {}
        rect_dict['id'] = self.id
        rect_dict['width'] = self.width
        rect_dict['height'] = self.height
        rect_dict['x'] = self.x
        rect_dict['y'] = self.y
        return rect_dict
