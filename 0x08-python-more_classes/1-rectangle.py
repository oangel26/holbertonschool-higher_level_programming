#!/usr/bin/python3
""" Module which creates a blueprint model for class Rectangle """


class Rectangle:
    """ class that defines a rectangle """
    def __init__(self, width=0, height=0):
        """ Constructor of the rectanglangle objects

        Args:
        width (int): width of rectangle.
        height (int): height of rectangle

        Raises:
        ValueError: if width or heigth is < 0.
        TypeError: if width or heigth are not integers.

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif type(value) is int and value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif type(value) is int and value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.width = "4"
    my_rectangle.height = 3
    print(my_rectangle.__dict__)
