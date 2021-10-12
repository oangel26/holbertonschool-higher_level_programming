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


if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(dir(r))

    try:
        print("Rectangle: {} - {}".format(r.width, r.height))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r2 = Rectangle(4, True)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
