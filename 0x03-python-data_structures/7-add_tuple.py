#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuplea_1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    tuplea_2 = tuple_a[1] if len(tuple_a) >= 2 else 0
    tupleb_1 = tuple_b[0] if len(tuple_b) >= 1 else 0
    tupleb_2 = tuple_b[1] if len(tuple_b) >= 2 else 0
    result = tuplea_1 + tupleb_1, tuplea_2 + tupleb_2
    return result
