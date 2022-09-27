#!/usr/bin/python3
"""Rectangle class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectange Geometry class"""

    def __init__(self, width, height):
        """Create rectangle object"""
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """String representation of rectangle object"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
