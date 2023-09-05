#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """
    Only allows the creation of an attribute called first_name
    """

    __slots__ = ["first_name"]
