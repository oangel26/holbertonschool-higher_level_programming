#!/usr/bin/python3
""" Module that prints a square """


def print_square(size):
    """ Function that prints a square with the character #

    Args:
    size: is the size length of the square

    Returns:
    Void

    Raises:
    - size must be an integer, otherwise raise a TypeError exception
    with the message size must be an integer.

    - if size is less than 0, raise a ValueError exception
    with the message size must be >= 0.

    - if size is a float and is less than 0, raise a TypeError exception
    with the message size must be an integer.
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("{}".format("#"), end="")
        print()


if __name__ == "__main__":
    print_square(4)
    print("")
    print_square(10)
    print("")
    print_square(0)
    print("")
    print_square(1)
    print("")
    try:
        print_square(-1)
    except Exception as e:
        print(e)
    print("")
