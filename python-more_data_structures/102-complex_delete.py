#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_deleted = []

    for k, v in a_dictionary.items():
        if v == value:
            keys_deleted.append(k)

    for key in keys_deleted:
        del a_dictionary[key]

    return a_dictionary
