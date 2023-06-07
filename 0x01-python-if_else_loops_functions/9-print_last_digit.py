#!/usr/bin/python3
def print_last_digit(number):
    h = 0
    if number < 0:
       number = -number
    h = 1
    lastd = number % 10
    if h == 1:
       number = -number
    print("{:d}".format(lastd), end="")
    return (lastd)
