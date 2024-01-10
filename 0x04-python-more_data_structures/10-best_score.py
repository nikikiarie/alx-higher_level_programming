#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    xv = 0
    xk = None
    for i, j in a_dictionary.items():
        if j > xv:
            xv = j
            xk = i
    return xk
