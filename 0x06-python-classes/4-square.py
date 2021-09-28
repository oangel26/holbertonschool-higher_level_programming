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
        self.__size = size

    def area(self):
        """ Public instance method

        Returns:
        Returns the current square area.

        """
        area = self.__size * self.__size
        return area

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value


if __name__ == "__main__":
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)
