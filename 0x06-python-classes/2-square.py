#!/usr/bin/python3
'''Define Square class with arg validation'''


class Square:
    '''Represents a Square class'''

    def __init__(self, size=0):
        '''Initialize a square'''
        if type(size) != 'int':
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
