#!/usr/bin/python3
"""Square class"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Init method"""
        self.__size = size
        self.__position = position

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    """Getter and setter"""
    @property
    def size(self):
        """property"""
        return self.__size

    @property
    def position(self):
        """ property"""
        return self.__position

    @size.setter
    def size(self, value):
        """setter"""
        if isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """setter"""
        if isinstance(value, tuple) and len(value) == 2 and isinstance(value[0], int) and isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
