#!/usr/bin/python3
"""defines a class called square"""


class Square:
    """ this class defines properties
    of a quare based on 0-square.py

    attributes:
        size is size of a square
    """
    def __init__(self, size):
        """creates new instance of a square
        arguments:
        size
        """
        self.__size = size
