#!/usr/bin/python3
def remove_char_at(string, n):
    if n < 0 or n >= len(string):
        return string
    result = ""
    i = 0
    while i < len(string):
        if i != n:
            result += string[i]
        i += 1
    return result
