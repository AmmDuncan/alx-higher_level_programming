#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = {**a_dictionary}
    for k, v in a_dictionary.items():
        if v == value:
            del new_dict[k]
    return new_dict
