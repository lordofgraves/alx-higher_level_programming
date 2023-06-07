#!/usr/bin/python3
def fizzbuzz():
    for fizzbuz in range(1, 101):
        if fizzbuz % 3 == 0:
            print("Fizz", end =" ")
        elif fizzbuz % 5 == 0:
            print("Buzz", end =" ")
        elif fizzbuz % 5 == 0 and fizzbuz % 3 == 0:
            print("FizzBuz", end=" ")
        else:
            print("{:d}".format(fizbuz), end =" ")
