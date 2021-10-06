#!/usr/bin/python3
""" Modules that divides elements of a matrix """


def matrix_divided(matrix, div):
    """ Function that divides all elements of a matrix

    Args:
    matrix: must be a list of lists of integers or floats
    div: must be a number (integer or float),

    Returns:
    Returns a new matrix

    Raises:
    - Each row of the matrix must be of the same size,
    otherwise raise a TypeError exception with the message Each
    row of the matrix must have the same size.

    - div must be a number (integer or float), otherwise raise a
    TypeError exception with the message div must be a number.

    - div can’t be equal to 0, otherwise raise a ZeroDivisionError
    exception with the message division by zero.
    """

    message = "matrix must be a matrix (list of lists) of integers/floats"
    if div is None:
        raise TypeError("div must be a number")
    if matrix is None:
        raise TypeError(message)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if len(matrix) == 0:
        raise TypeError(message)

    new_matrix = []
    len_row = len(matrix[0])

    for row in matrix:
        new_list = []
        if len_row != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        if len(row) == 0:
            raise TypeError(message)
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError(message)
            else:
                new_list.append(round((i / div), 2))
        new_matrix.append(new_list)
    return new_matrix


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, 3))
    print(matrix)
