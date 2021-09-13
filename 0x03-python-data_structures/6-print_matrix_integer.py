#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Function that prints a matrix of integers"""
    for row in matrix:
        count = 0
        for i in row:
            count += 1
            if count != len(row):
                print("{:d}".format(i), end=" ")
            else:
                print("{:d}".format(i), end="")
        print()

if __name__ == "__main__":
    matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()
