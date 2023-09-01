#!/usr/bin/python3

"""
Module composed by a function that prints 2 new lines after ".?:" characters
"""


def text_indentation(text):
    """ Function that prints 2 new lines after ".?:" characters
    Args:
        text: input string
    Raises:
        TypeError: If text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    string = text[:]

    for a in ".?:":
        text_list = string.split(a)
        string = ""
        for i in text_list:
            i = i.strip(" ")
            string = i + a if string is "" else string + "\n\n" + i + a

    print(string[:-3], end="")
