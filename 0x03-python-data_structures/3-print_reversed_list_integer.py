#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Function that prints all integers of a list, in reverse order."""
    if my_list == []:
        return None
    else:
        for i in reversed(my_list):
            print("{:d}".format(i))

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print_reversed_list_integer(my_list)
