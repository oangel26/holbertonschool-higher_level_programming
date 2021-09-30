#!/usr/bin/python3
""" Module which creates a blueprint model for class Rectangle """


class Rectangle:
    """ class that defines a rectangle """
    pass


if __name__ == "__main__":
    my_rectangle = Rectangle()
    print(type(my_rectangle))
    print(my_rectangle.__dict__)
    print(__name__)
    print(my_rectangle.__doc__)
