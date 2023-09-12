#!/usr/bin/python3
"""This module defines an appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
