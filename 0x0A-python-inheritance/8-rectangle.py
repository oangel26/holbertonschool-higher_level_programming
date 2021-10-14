#!/usr/bin/python3
""" Module that represents class BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Subclass of BaseGeometry that represents a Rectangle """

    def __init__(self, width, height):
        """ Constructor method of Rectangle class objects """
        self.__height = height
        self.__width = width
        super().integer_validator("width", width)
        super().integer_validator("height", height)


if __name__ == "__main__":
    print(issubclass(Rectangle, BaseGeometry))

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
