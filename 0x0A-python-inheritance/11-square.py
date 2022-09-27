#!/usr/bin/python3
"""Square class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Instantiate Sqaure object"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculate area of square"""
        return self.__size**2

    def __str__(self):
        """String representation of square object"""
        return "[Square] {}/{}".format(self.__size, self.__size)
