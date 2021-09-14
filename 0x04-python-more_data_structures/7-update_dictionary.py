#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Function that replaces or adds key/value in a dictionary."""
    a_dictionary[key] = value
    return a_dictionary

def print_sorted_dictionary(a_dictionary):
    """Function that prints a dictionary by ordered keys."""
    sorted_keys_list = sorted(a_dictionary.keys())
    for i in sorted_keys_list:
        print("{}: {}".format(i, a_dictionary[i]))

if __name__ == "__main__":
    a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
    new_dict = update_dictionary(a_dictionary, 'language', "Python")
    print_sorted_dictionary(new_dict)
    print("--")
    print_sorted_dictionary(a_dictionary)

    print("--")
    print("--")

    new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
    print_sorted_dictionary(new_dict)
    print("--")
    print_sorted_dictionary(a_dictionary)
