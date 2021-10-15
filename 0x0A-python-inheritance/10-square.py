#!/usr/bin/python3
""" Module that represents class BaseGeometry """
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle, BaseGeometry):
    """ Class that represents a square """

    def __init__(self, size):
        """ Constructor method of Square class objects """
        self.__size = size
        super().integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)


    """
    def integer_validator(self, name, value):
        Public instance method that validates value

    if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
    """
    def area(self):
        """ Public instance method that return the area of a Square """
        return (super().area())


if __name__ == "__main__":
    s = Square(13)
    print(s.__dict__)
    print(s)
