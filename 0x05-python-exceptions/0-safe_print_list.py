#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0
    try:
        while printed < x:
            print("{}".format(my_list[printed]), end="")
            printed += 1
        print("\n", end="")
        return printed
    except:
        print("\n", end="")
        return printed
