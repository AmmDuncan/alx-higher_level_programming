#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = argv[1:]
    args_len = len(args)
    print("{} arguments{}".format(args_len, ":" if args_len > 0 else '.'))

    for index, arg in enumerate(args):
        print("{}: {}".format(index + 1, arg))
