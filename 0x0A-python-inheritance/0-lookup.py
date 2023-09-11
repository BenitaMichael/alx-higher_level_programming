#!/usr/bin/python3
"""
    This module returns the list of available attributes
    and methods and takes in the arg: obj
"""


def lookup(obj):
    """This function returns all attributes and methods of an object"""
    return dir(obj)
