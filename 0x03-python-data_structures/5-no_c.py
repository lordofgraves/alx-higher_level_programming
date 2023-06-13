#!/usr/bin/python3
def no_c(my_string):
    cr = "cC"
    new_string = ""
    for char in my_string:
        if char != cr:
            new_string += char
    return new_string
