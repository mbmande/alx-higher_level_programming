#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    temp = a_dictionary.copy()
    for i, j in temp.items():
        if value == j:
            a_dictionary.pop(i)
    return a_dictionary
