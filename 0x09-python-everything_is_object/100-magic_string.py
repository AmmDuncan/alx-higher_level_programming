#!/usr/bin/python3
def magic_string():
    magic_string.counter = magic_string.__dict__.setdefault('counter', -1) + 1
    return ", ".join(["BestSchool"] * magic_string.counter)
