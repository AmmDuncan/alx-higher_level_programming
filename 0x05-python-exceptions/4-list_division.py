#!/usr/bin/python3
from decimal import DivisionByZero


def list_division(my_list_1, my_list_2, list_length):
    res = [0] * list_length
    for i in range(list_length):
        try:
            res[i] = my_list_1[i] / my_list_2[i]
        except (TypeError):
            res[i] = 0
            print("wront type")
        except (ZeroDivisionError):
            res[i] = 0
            print("division by 0")
        except (IndexError):
            res[i] = 0
            print("out of range")
    return res
