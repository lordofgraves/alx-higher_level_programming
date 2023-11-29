#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """
    Class that defines properties of rectangle (based on 0-rectangle.py).

    Attributes:
        width (int)
        height (int)
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """creates new instances of Rectangle.

        Args:
            width (int, optional): Defaults to 0.
            height (int, optional): Defaults to 0.
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        """retrive width.

        Returns:
            the width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """retrive height.

        Returns:
            the height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Property setter.

        Args:
            width of the rectangle.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Property setter.

        Args:
            height of the rectangle.

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns the rectangle area

        Returns:
            int: area.
        """
        return self.__height * self.__width

    def perimeter(self):
        """returns the rectangle perimeter

        Returns:
            int: perimeter.
        """
        if self.__height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """prints the rectangle with the character # .

        Returns:
            str: the rectangle
        """
        rec = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                rec.append("#")
                if j < self.__width - 1:
                    rec.append("")
                    
            if i < self.__height - 1:
                rec.append("\n")

        return "".join(rec)
    
    def __repr__(self):
        """string representation of the rectangle.

        Returns:
            the rectangle representation.
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
    
    def __del__(self):
        """Deletes a rectangle.
        """
        print("{:s}".format("Bye rectangle..."))
        type(self).number_of_instances -= 1
