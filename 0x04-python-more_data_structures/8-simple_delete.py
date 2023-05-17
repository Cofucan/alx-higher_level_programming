#!/usr/bin/python3

def simple_delete(a_dictionary: dict, key=""):
    if key in a_dictionary:
        a_dictionary.pop(key)
    return a_dictionary
