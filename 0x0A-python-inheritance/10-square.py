#!/usr/bin/python3
""" Module that represents class BaseGeometry """


class BaseGeometry:
    """ Class that represents the BaseGeometry """

    def area(self):
        """ Public instance method: that raises an Exception
        with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Public instance method that validates value

        Args:
        name: (str) name of integer
        value: (int) integer to validate

        Raises:
        * If value is not an integer: raise a TypeError exception
        * if value is less or equal to 0: raise a ValueError exception
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Class that represents a Rectangle """

    def __init__(self, width, height):
        """ Constructor method of Rectangle class objects """
        self.__height = height
        self.__width = width
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        """ Public instance method that return the area of the rectangle """
        return (self.__width * self.__height)

    def __str__(self):
        """ return description: [Rectangle] <width>/<height> """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """ Class that represents a square """

    def __init__(self, size):
        """ Constructor method of Square class objects """
        super().__init__(size, size)
        super().integer_validator("size", size)

    def area(self):
        """ Public instance method that return the area of a Square """
        return (super().area())


if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())
