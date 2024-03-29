#!/usr/bin/python3
"""Square class"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """initialize size"""
        self.__size = size

    def area(self):
        """return the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """print the square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
    """getter and setter for size"""
    @property
    def size(self):
        """return the size"""
        return self.__size
    """setter for size"""
    @size.setter
    def size(self, value):
        """set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
