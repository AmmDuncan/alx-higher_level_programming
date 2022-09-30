#!/usr/bin/python3
"""Define Rectange class"""
from models.base import Base
from utils.validators import is_positive_integer, is_non_negative_integer


class Rectangle(Base):
    """Representation of Rectange"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiate Rectange object"""
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

    def area(self):
        """Calculate area of rectangle"""
        return self.__width * self.__height

    def display(self):
        h = self.__height
        w = self.__width
        for _ in range(h):
            print("#" * w)
