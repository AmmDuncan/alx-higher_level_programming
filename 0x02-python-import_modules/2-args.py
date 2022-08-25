#!/usr/bin/python3
from sys import argv

args = argv[1:]
args_len = len(args)
if __name__ == "__main__":
    is_zero = args_len == 0
    is_one = args_len == 1
    print("{} argument{}{}".format(args_len,'s' if not is_one else '', ":" if not is_zero else '.'))

    for i in range(args_len):
        print("{}: {}".format(i + 1, args[i]))
