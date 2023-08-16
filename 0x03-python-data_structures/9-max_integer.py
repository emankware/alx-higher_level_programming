#!/usr/bin/python3
# 9-max_integer.py

def max_integer(my_list=[]):
    if not my_list:
        return None

    max_integer = my_list[0]
    for i in my_list:
        if i > max_integer:
            max_integer = i
    return max_integer
