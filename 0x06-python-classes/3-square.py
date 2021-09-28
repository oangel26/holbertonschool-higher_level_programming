#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Module which represents the model of a Square """


class Square:
    """ Class that defines the model of a square """
    def __init__(self, size=0):
        """ Constructor of the square:
        Args:
        size (int): size of the square.

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Public instance method

        Returns:
        Returns the current square area.

        """
        area = self.__size * self.__size
        return area


if __name__ == "__main__":
    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    my_square_2 = Square(5)
    print("Area: {}".format(my_square_2.area()))
