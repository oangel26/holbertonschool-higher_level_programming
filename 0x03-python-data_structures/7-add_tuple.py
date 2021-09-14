#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Function that adds 2 tuples"""
    if len(tuple_a) == 0:
        tuple_a = 0, 0
    if len(tuple_b) == 0:
        tuple_b = 0, 0
    if len(tuple_a) == 1:
        tuple_a = tuple_a[0], 0
    if len(tuple_b) == 1:
        tuple_b = tuple_b[0], 0
    if len(tuple_a) >= 2:
        tuple_a = tuple_a[0], tuple_a[1]
    if len(tuple_b) >= 2:
        tuple_b = tuple_b[0], tuple_b[1]
    new_tuple = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return new_tuple


if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1, 0)))
    print(add_tuple(tuple_a, ()))
