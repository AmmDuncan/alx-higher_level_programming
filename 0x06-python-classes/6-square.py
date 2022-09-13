#!/usr/bin/python3
'''Define Square class with validation and area methods'''


from multiprocessing.sharedctypes import Value
from wsgiref import validate


class Square:
    '''Square class'''

    def __init__(self, size=0, position=(0, 0)):
        '''Initialize Square object'''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = position
        if (x < 0 or y < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def area(self):
        '''Get area of square'''
        return self.__size**2

    @property
    def size(self):
        '''Get size attr'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Set size attr'''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if Value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''Get position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''Set position'''
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if (x < 0 or y < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        '''Print square'''
        if self.size == 0:
            print()
        else:
            x, y = self.position
            for _ in range(y):
                print()
            for i in range(self.size):
                for _ in range(x):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print()
