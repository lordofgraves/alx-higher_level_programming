#!/usr/bin/python3
def fizzbuzz():
    for fizzbuzz in range(0, 101, 1):
    if fizzbuzz % 3 == 0:
        print("Fizz ", end = '')
    elif fizzbuzz % 5 == 0:
        print("Buzz ", end = '')
    elif fizzbuzz % 5 == 0 and fizzbuzz % 3 == 0:
        print("FizzBuzz")
    else:
        print("{:d} ".format(fizzbuzz), end = '')
