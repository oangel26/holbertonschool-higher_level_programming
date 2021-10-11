#!/usr/bin/python3
""" Module of function that returns methods and attributes of objs """


def lookup(obj):
    """ Function that returns the list of available
    attributes and methods of an object.

    Args:
    obj: object

    Returns:
    Returns a list object
    """
    return dir(obj)


if __name__ == "__main__":
    class MyClass1(object):
        pass

    class MyClass2(object):
        my_attr1 = 3
        def my_meth(self):
            pass

    print(lookup(MyClass1))
    print(lookup(MyClass2))
    print(lookup(int))
