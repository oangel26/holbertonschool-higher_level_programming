#!/usr/bin/python3
""" Module looks if an abjects is a sub class of """


def inherits_from(obj, a_class):
    """ Function that returns True if the object is an instance
    of a class that inherited (directly or indirectly) from the
    specified class ; otherwise False.

    Args:
    obj: object
    a_class: class type

    Returns:
    returns True if the object is an instance of a class that inherited
    (directly or indirectly); otherwise False
    """
    if (issubclass(obj.__class__, a_class)):
        if (obj.__class__ is a_class):
            return (False)
        return (True)


if __name__ == "__main__":
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
