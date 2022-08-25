#!/usr/bin/python3
from sys import argv

args = argv[1:]
args_len = len(args)
if __name__ == "__main__":
    print("{} arguments{}".format(args_len, ":" if args_len > 0 else '.'))

    for i in range(args_len):
        print("{}: {}".format(i + 1, args[i]))
