#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Module which represents the model of a Square """


class Square(object):
    """ Class that defines the model of a square """
    def __init__(self, size=0, position=(0, 0)):
        """ Constructor of the square:
        Args:
        size (int): size of the square.
        position (int, int): tuple of int. position of the squere

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        TypeError: if touple is not 2 positive integers

        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Public instance method

        Returns:
        Returns the current square area.

        """
        area = self.__size ** 2
        return area

    def my_print(self):
        """ Public instance method

        Prints in stdout the square with the character #

        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(self.__position[0] * " ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()


if __name__ == "__main__":
    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()

    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("--")
