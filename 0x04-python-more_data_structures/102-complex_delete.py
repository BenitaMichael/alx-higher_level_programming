#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    new_keys = list(a_dictionary.keys())

    for dic_val in new_keys:
        if value == a_dictionary.get(dic_val):
            del a_dictionary[dic_val]

    return (a_dictionary)
