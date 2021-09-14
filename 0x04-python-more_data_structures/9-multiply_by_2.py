#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Function that returns a new dictionary with all values multiplied by 2"""
    new_dict = {}
    for k, v in a_dictionary.items():
        new_dict[k] = v * 2
    return new_dict

def print_sorted_dictionary(a_dictionary):
    """Function that prints a dictionary by ordered keys."""
    sorted_keys_list = sorted(a_dictionary.keys())
    for i in sorted_keys_list:
        print("{}: {}".format(i, a_dictionary[i]))

if __name__ == "__main__":
    a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
    new_dict = multiply_by_2(a_dictionary)
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)
