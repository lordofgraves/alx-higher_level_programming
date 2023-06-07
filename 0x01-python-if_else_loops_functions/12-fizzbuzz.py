#!/usr/bin/python3
def fizzbuzz():
    for fizzbuz in range(1, 101):
        if fizzbuz % 3 == 0 and fizzbuz % 5 == 0:
            print("FizzBuzz", end=" ")
        elif fizzbuz % 3 == 0:
            print("Fizz", end =" ")
        elif fizzbuz % 5 == 0:
            print("Buzz", end =" ")
        else:
            print("{:d}".format(fizzbuz), end =" ")
