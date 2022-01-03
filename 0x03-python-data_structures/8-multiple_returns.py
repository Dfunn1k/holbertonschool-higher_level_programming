#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        result_tuple = (len(sentence), None)
    else:
        result_tuple = (len(sentence), sentence[0])

    return(result_tuple)
