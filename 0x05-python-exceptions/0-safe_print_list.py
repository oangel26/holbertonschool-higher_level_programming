#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """ function that prints x elements of a list. """
    try:
        counter = 0
        for i in my_list:
            if counter < x:
                counter += 1
                print("{}".format(i), end="")
            else:
                break
        print()
        return (counter)
    except TypeError:
        print("Oops!  That was no valid number.  Try again...")
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
