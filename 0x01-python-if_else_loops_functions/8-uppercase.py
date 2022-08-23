#!/usr/bin/python3
def uppercase(str):
    length = len(str)
    for i, c in enumerate(str):
        islast = i == length - 1
        print("{:c}".format(ord(c) - 32 if islower(c)
              else ord(c)), end="")
    print("")


def islower(c):
    num = ord(c)
    return (num > 96 and num < 96 + 27)
