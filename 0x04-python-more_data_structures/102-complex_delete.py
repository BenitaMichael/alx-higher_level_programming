#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    new_keys = list(a_dictionary.keys())

    for val in new_keys:
        if value == a_dictionary.get(val):
            del a_dictionary[val]

    return (a_dictionary)
