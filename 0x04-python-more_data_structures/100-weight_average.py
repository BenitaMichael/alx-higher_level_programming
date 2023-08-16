#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    mult = 0
    add = 0

    for tup in my_list:
        mult += tup[0] * tup[1]
        add += tup[1]

    return (mult / add)
