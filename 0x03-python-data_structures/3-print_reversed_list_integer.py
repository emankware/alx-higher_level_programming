#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return

    my_list.reverse()
    for number in my_list:
        print("{:d}".format(number))
