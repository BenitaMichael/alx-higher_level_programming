#!/usr/bin/python3

def uniq_add(my_list=[]):
    add_list = set(my_list)
    num = 0

    for i in add_list:
        num += i

    return (num)
