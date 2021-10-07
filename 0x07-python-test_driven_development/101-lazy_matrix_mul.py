#!/usr/bin/python3
""" Module function that multiplies 2 matrices """


import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
    for j in m_b:
        if type(j) is not list:
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row_a in m_a:
        for i in row_a:
            if type(i) is not int and type(i) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for row_b in m_b:
        for j in row_b:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_b should contain only integers or floats")
    len_row_a = len(m_a[0])
    len_row_b = len(m_b[0])
    for row_a in m_a:
        if len(row_a) != len_row_a:
            raise TypeError("each row of m_a must be of the same size")
    for row_b in m_b:
        if len(row_b) != len_row_b:
            raise TypeError("each row of m_b must be of the same size")
    if len_row_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = np.dot(m_a, m_b)
    return (new_matrix)


if __name__ == "__main__":
    print(lazy_matrix_mul([[1, 2]], [[1, 2], [1, 2, 3]]))
