#!/usr/bin/python3
""" Module that checks for exact same object """


def is_same_class(obj, a_class):
    """ Function that returns True if the object is exactly an
    instance of the specified class ; otherwise False.

    Args:
    obj: object
    a_class: type of class

    Returns:
    returns True if the object is exactly an instance, otherwise False
    """
    if (isinstance(obj, a_class)):
        if (obj.__class__ is a_class):
            return (True)
        else:
            return (False)
    else:
        return (False)


if __name__ == "__main__":
    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
    a = True
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, object.__name__))
    a = 3.14
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, object.__name__))
    a = True
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
    a = None
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, object.__name__))
    a = None
    if is_same_class(a, list):
        print("{} is an instance of the class {}".format(a, object.__name__))
    a = [1, 2, 3]
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
