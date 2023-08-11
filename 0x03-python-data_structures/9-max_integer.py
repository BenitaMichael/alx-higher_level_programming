#!/usr/bin/python3

def max_integer(my_list=[]):
    list_length = len(my_list)

    if list_length == 0:
        return (None)

    max_int = my_list[0]

    for i in range(1, list_length):
        if my_list[i] > max_int:
            max_int = my_list[i]

    return (max_int)
