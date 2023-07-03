#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for y, element in enumerate(row):
            if y == len(row) - 1:
                print("{:d}".format(element), end="")
            else:
                print("{:d} ".format(element), end="")
        print()
