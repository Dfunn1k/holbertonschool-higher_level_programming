#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        result_tuple = (0, None)
    else:
        result_tuple = (len(sentence), sentence[0])

    return(result_tuple)
