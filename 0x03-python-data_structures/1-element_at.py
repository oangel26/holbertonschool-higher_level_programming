#!/usr/bin/python3
def element_at(my_list, idx):
    """Function that retrieves an element from a list like in C."""
    if idx < 0:
        return None
    elif idx >= len(my_list):
        return None
    else:
        return my_list[idx]

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
