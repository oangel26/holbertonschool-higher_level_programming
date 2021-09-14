#!/usr/bin/python3
def max_integer(my_list=[]):
    """Function that finds the biggest integer of a list."""
    if my_list == []:
        return None
    else:
        max_n = my_list[0]
        for i in my_list:
            if max_n < i:
                max_n = i
        return max_n

if __name__ == "__main__":
    my_list = [1, 90, 2, 13, 34, 5, -13, 3]
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))
