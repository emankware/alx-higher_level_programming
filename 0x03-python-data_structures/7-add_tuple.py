#!/usr/bin/python3
# 7-add_tuple.py

def add_tuple(tuple_a=(), tuple_b=()):
    len1 = tuple_a + (0, 0)
    len2 = tuple_b + (0, 0)

    results1 = 0
    results2 = 0

    results1 += len1[0] + len2[0]
    results2 += len1[1] + len2[1]

    return (results1, results2)
