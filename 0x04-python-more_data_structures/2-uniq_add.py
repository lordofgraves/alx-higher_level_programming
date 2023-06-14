#!/usr/bin/python3
def uniq_add(my_list=[]):
    from functools import reduce
    uniq_elem = []
    for element in my_list:
        if element not in uniq_elem:
            uniq_elem.append(element)
    reslt = reduce(lambda x, y: x + y, uniq_elem)
    return reslt
