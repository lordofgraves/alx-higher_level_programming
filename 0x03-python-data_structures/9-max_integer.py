#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        a = my_list[0]
        idx = 1
        while idx < len(my_list):
            if a < my_list[idx]:
                a = my_list[idx]
            idx += 1
        return a
    else:
        return None
