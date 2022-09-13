#!/usr/bin/python3
'''Define Square class with validation and area methods'''


class Square:
    '''Square class'''

    def __init__(self, size=0):
        '''Initialize Square object'''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size**2
