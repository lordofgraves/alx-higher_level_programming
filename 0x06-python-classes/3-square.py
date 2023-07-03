#!/usr/bin/python3
"""A module that defines a square"""


class Square:
    """A class that defines a square"""
    def __init__(self, size=0):
        """Instantiation with size

        Args:
            size (int): The size of the new square
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    """Returns the area of the square"""
    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
