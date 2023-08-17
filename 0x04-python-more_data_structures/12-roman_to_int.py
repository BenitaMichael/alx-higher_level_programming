#!/usr/bin/python3

def subtraction(list_num):
    minus = 0
    max_list = max(list_num)

    for i in list_num:
        if max_list > i:
            minus += i

    return (max_list - minus)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(roman_n.keys())

    num = 0
    last = 0
    num_list = [0]

    for c in roman_string:
        for r_num in list_keys:
            if r_num == c:
                if roman_n.get(c) <= last:
                    num += subtraction(num_list)
                    num_list = [roman_n.get(c)]
                else:
                    num_list.append(roman_n.get(c))

                last = roman_n.get(c)

    num += subtraction(num_list)

    return (num)
