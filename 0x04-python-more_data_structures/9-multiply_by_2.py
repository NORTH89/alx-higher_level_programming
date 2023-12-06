#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for i in list(a_dictionary.keys()):
        new[i] *= 2
    return new
