#!/usr/bin/python3
'''Define Square class with validation and area methods'''


class Square:
    '''Square class'''

    def __init__(self, size=0, position=(0, 0)):
        '''Initialize Square object'''
        validate_size(size)
        validate_position(position)
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
        validate_size(value)
        self.__size = value

    @property
    def position(self):
        '''Get position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''Set position'''
        validate_position(value)
        self.__position = value

    def my_print(self):
        '''Print square'''
        if self.size == 0:
            print()
        else:
            x, y = self.position
            for _ in range(y):
                print()
            for _ in range(self.size):
                for _ in range(x):
                    print(" ", end="")
                for _ in range(self.size):
                    print("#", end="")
                print()

    def __str__(self):
        '''String representation of square'''
        str_rep = ""
        x, y = self.position
        for _ in range(y):
            str_rep += "\n"
        for i in range(self.size):
            for _ in range(x):
                str_rep += " "
            for _ in range(self.size):
                str_rep += "#"
            if i < self.size - 1:
                str_rep += "\n"
        return str_rep

    def __repr__(self):
        '''String representation of square'''
        return f"Square({self.size}, {self.position})"


def validate_size(size):
    '''Validate size of square'''
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError("size must be >= 0")


def validate_position(position):
    '''Validate position of square'''
    if not isinstance(position, tuple):
        raise_position_exception()
    if len(position) != 2:
        raise_position_exception()
    x, y = position
    if not isinstance(x, int) or not isinstance(y, int):
        raise_position_exception()
    if (x < 0 or y < 0):
        raise_position_exception()


def raise_position_exception():
    '''Raise position exception'''
    raise TypeError("position must be a tuple of 2 positive integers")
