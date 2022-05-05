#!/usr/bin/python3
def best_score(a_dictionary):
    """Return a key with the biggest integer value"""
    if a_dictionary is None:
        return None

    value_Match = sorted(a_dictionary.values(), reverse=True)

    for keys, values in a_dictionary.items():
        if values == value_Match[0]:
            return keys
