#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = argv[1:]
    args_len = len(args)
    is_zero = args_len == 0
    is_one = args_len == 1
    sval = 's' if not is_one else ''
    sign = ":" if not is_zero else '.'
    print("{} argument{}{}".format(args_len, sval, sign))

    for i in range(args_len):
        print("{}: {}".format(i + 1, args[i]))
