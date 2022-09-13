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
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()
