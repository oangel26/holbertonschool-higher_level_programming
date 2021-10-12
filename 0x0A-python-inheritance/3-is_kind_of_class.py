#!/usr/bin/python3
""" Module that checks if object is from same class or inhgerit from """


def is_kind_of_class(obj, a_class):
    """ unction that returns True if the object is an
    instance of, or if the object is an instance of a
    class that inherited from, the specified class;
    otherwise False.

    Args:
    obj: object
    a_class: class type

    Returns:
    returns True if the object is an instance specified class or inherits
    from; otherwise False.
    """
    return (isinstance(obj, a_class))


if __name__ == "__main__":
    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))
