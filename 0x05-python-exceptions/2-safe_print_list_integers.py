#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """ function that prints the first x elements
    of a list and only integers
    """
    try:
        count = 0
        for i in range(x):
            if type(my_list[i]) == int:
                count += 1
                print("{:d}".format(my_list[i]), end="")
            else:
                continue
        print()
        return (count)
    except IndexError:
        print("List index out of range")


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list_integers(my_list, 2)
    print("nb_print: {:d}".format(nb_print))

    my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
    nb_print = safe_print_list_integers(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))

