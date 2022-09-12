#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if not value:
            return False
        print("{:d}".format(value))
        return True
    except (ValueError):
        return False
