#!/usr/bin/python3
""" A class that defines a square """


class Square:
    """
    A class that defines a square based on 1-square.py

    Attributes:
        size (int): The size of the square.
    """
    def __init__(self, size=0):
        """ Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
