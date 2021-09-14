#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """Function that returns a list with all values multiplied
    by a number without using any loops.
    """
    new_list = list(map(lambda x: x * number, my_list))
    return new_list

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 6]
    new_list = multiply_list_map(my_list, 4)
    print(new_list)
    print(my_list)
