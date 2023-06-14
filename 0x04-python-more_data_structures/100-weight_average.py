#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    num = 0
    den = 0
    i = 0
    while i < len(my_list):
        score, weight = my_list[i]
        num += score * weight
        den += weight
        i += 1
    return num / den
