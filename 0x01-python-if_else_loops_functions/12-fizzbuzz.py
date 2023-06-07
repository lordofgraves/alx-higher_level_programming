#!/usr/bin/python3
def fizzbuzz():
    for fizzbuzz in range(0, 101, 1):
        if fizzbuzz % 3 == 0:
            print("Fizz ", end = '')
        elif fizzbuzz % 5 == 0:
            print("buzz ", end = '')
        else:
            print("{:d} ".format(fizzbuzz), end = '')
    return (fizzbuzz)
