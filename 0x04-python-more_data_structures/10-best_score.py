#!/usr/bin/python3
def best_score(a_dictionary):
    if not len(list(a_dictionary)) or not a_dictionary.items()[0][1]:
        return None
    highest_key = list(a_dictionary)[0]
    for key, value in a_dictionary.items():
        if value > a_dictionary[highest_key]:
            highest_key = key
    return highest_key
