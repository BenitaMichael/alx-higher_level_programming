#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0:
        return (None)

    list_lenght = len(my_list)

    if idx > list_lenght + 1:
        return (None)

    return (my_list[idx])
