#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = [0] * list_length
    err = None
    for i in range(list_length):
        try:
            res[i] = my_list_1[i] / my_list_2[i]
        except (TypeError):
            err = "wrong type"
        except (ZeroDivisionError):
            err = "division by 0"
        except (IndexError):
            err = "out of range"
        finally:
            if (err is not None):
                print(err)
                err = None
    return res
