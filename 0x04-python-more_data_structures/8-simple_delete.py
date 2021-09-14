#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Function that deletes a key in a dictionary."""
    if key in a_dictionary.keys():
        del(a_dictionary[key])
        return a_dictionary
    return a_dictionary

def print_sorted_dictionary(a_dictionary):
    """Function that prints a dictionary by ordered keys."""
    sorted_keys_list = sorted(a_dictionary.keys())
    for i in sorted_keys_list:
        print("{}: {}".format(i, a_dictionary[i]))

if __name__ == "__main__":
    a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
    new_dict = simple_delete(a_dictionary, 'track')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)

    print("--")
    print("--")
    new_dict = simple_delete(a_dictionary, 'c_is_fun')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)

