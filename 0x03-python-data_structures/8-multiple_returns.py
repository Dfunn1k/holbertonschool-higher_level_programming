#!/usr/bin/python3
def multiple_returns(sentence):
    """Return a tuple with the lenght of a
    string and its first character"""

    if sentence is None:
        tuple_result = (0, None)
    else:
        tuple_result = (len(sentence), sentence[0])

    return tuple_result
