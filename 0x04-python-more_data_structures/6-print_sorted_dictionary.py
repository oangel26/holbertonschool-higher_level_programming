#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Function that prints a dictionary by ordered keys."""
    sorted_keys_list = sorted(a_dictionary.keys())
    for i in sorted_keys_list:
        print("{}: {}".format(i, a_dictionary[i]))

if __name__ == "__main__":
    a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
    print_sorted_dictionary(a_dictionary)
