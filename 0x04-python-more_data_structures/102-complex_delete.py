#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Function that deletes keys with a specific value in a dictionary."""
    list_keys_to_del = []
    for k, v in a_dictionary.items():
        if v == value:
            list_keys_to_del.append(k)

    for i in list_keys_to_del:
        del a_dictionary[i]

    return a_dictionary

def print_sorted_dictionary(a_dictionary):
    """Function that prints a dictionary by ordered keys."""
    sorted_keys_list = sorted(a_dictionary.keys())
    for i in sorted_keys_list:
        print("{}: {}".format(i, a_dictionary[i]))

if __name__ == "__main__":
    a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
    new_dict = complex_delete(a_dictionary, 'C')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)

    print("--")
    print("--")
    new_dict = complex_delete(a_dictionary, 'c_is_fun')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)
