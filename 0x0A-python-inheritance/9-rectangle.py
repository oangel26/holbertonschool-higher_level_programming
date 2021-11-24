#!/usr/bin/python3
""" Module that represents class BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class that represents a Rectangle """

    def __init__(self, width, height):
        """ Constructor method of Rectangle class objects """
        self.__height = height
        self.__width = width
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def area(self):
        """ Public instance method: that raises an Exception
        with the message area() is not implemented
        """
        return (self.__width * self.__height)

    def __str__(self):
        """ return description: [Rectangle] <width>/<height> """
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__width, self.__height)


if __name__ == "__main__":
    r = Rectangle(3, 5)
    
    print(r)
    print(r.area())
