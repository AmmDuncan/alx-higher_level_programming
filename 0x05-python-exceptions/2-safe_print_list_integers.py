#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = i = 0
    if my_list is None:
        return printed
    try:
        while (printed < x):
            try:
                print("{:d}".format(my_list[i]), end="")
                printed += 1
                i += 1
            except (ValueError, TypeError):
                i += 1
                continue
            except (IndexError):
                break
        print("")
        return printed
    except (ValueError, TypeError):
        return printed
