#!/usr/bin/python3
"""Module to use Rectangle class with area and perimeter methods"""

Rectangle = __import__("2-rectangle").Rectangle

my_rect = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rect.area(), my_rect.perimeter()))

print("--")

my_rect.width = 10
my_rect.height = 3
print("Area: {} - Perimeter: {}".format(my_rect.area(), my_rect.perimeter()))
