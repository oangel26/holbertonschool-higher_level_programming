#!/usr/bin/python3
""" Module containing integers addition functions """


def add_integer(a, b=98):
    """ Function that adds 2 integers
    Args:
    a: integer a
    b: integer b (initialized by defect in 98)

    Returns:
    Returns an integer: the addition of a and b

    Raises:
    a and b must be integers or floats,
    otherwise raise a TypeError exception
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    elif a is None:
        raise TypeError("a must be an integer")
    else:
        result = a + b
        if result == float('inf') of resutl == -float('inf'):
            return 89
        return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
    print(add_integer(1, 2))
    print(add_integer(100, -2))
    print(add_integer(2))
    print(add_integer(100.3, -2))  # negative number test
    print(add_integer(100.3, 2 + 5j))  # complex number test
    print(add_integer(100.3, (2, 3)))  # tuple teste
    print(add_integer(2, [1, 2, 3]))  # List test
    print(add_integer(2, {'a': 1, 'b': 2}))  # dictionary test

    try:
        print(add_integer(4, "School"))
    except Exception as e:
        print(e)
    try:
        print(add_integer(None))
    except Exception as e:
        print(e)
