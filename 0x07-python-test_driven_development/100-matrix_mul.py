#!/usr/bin/python3

"""
Module composed by a function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices
    Args:
        m_a: matrix a
        m_b: matrix b
    Returns:
        multiplied integers
    Raises:
        TypeError: if m_a or m_b aren't a list
        TypeError: if m_a or m_b aren't a list of a lists
        TypeError: if the lists of m_a or m_b don't have integers or floats
        TypeError: if the rows of m_a or m_b don't have the same size
        
        ValueError: if m_a or m_b are empty
        ValueError: if m_a and m_b can't be multiplied
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for elements in m_a:
        if not isinstance(elements, list):
            raise TypeError("m_a must be a list of lists")

    for elements in m_b:
        if not isinstance(elements, list):
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for lists in m_a:
        for elements in lists:
            if not type(elements) in (int, float):
                raise TypeError("m_a should contain only integers or floats")

    for lists in m_b:
        for elements in lists:
            if not type(elements) in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    lenght = 0

    for elements in m_a:
        if lenght != 0 and lenght != len(elements):
            raise TypeError("each row of m_a must be of the same size")
        lenght = len(elements)

    lenght = 0

    for elements in m_b:
        if lenght != 0 and lenght != len(elements):
            raise TypeError("each row of m_b must be of the same size")
        lenght = len(elements)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    row = []
    col = 0

    for a in m_a:
        row_1 = []
        col_1 = 0
        num = 0
        while (col_1 < len(m_b[0])):
            num += a[col] * m_b[col][col_1]
            if col == len(m_b) - 1:
                col = 0
                col_1 += 1
                row_1.append(num)
                num = 0
            else:
                col += 1
        row.append(row_1)

    return row
