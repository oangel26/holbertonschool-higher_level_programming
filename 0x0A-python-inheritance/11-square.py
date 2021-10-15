#!/usr/bin/python3
""" Module that represents class BaseGeometry """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class that represents a square """

    def __init__(self, size):
        """ Constructor method of Square class objects """
        self.__size = size
        super().integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """ Public instance method that return the area of a Square """
        return (super().area())


if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())
