#!/usr/bin/python3
def uppercase(str):
    length = len(str)
    for i, c in enumerate(str):
        islast = i == length - 1
        if islower(c):
            print("{:c}".format(ord(c) - 32), end=("\n" if islast else ""))
        else:
            print(c, end=("\n" if islast else ""))


def islower(c):
    num = ord(c)
    return (num > 96 and num < 96 + 27)
