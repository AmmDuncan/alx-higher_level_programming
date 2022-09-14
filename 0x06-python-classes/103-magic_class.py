#!/usr/bin/python3
'''Define magic class'''
import math


class MagicClass:
    '''Represents magic class'''

    def __init__(self, radius):
        '''Initialize MagicClass object'''
        if type(radius) is not int and type(radius is not float):
            raise TypeError('radius must be a number')
        else:
            self.radius = radius

    def area(self):
        '''Calculate area of object'''
        return self.radius**2 * math.pi

    def circumference(self):
        '''Calculate circumference of object'''
        return 2 * math.pi * self.radius
