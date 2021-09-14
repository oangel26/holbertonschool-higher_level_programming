#!/usr/bin/python3
def best_score(a_dictionary):
    """Function that returns a key with the biggest integer value."""
    if a_dictionary is None or a_dictionary == {}:
        return None
    else:
        dict_sorted_keys = sorted(a_dictionary.keys())
        max_value = a_dictionary[dict_sorted_keys[0]]
        for k in dict_sorted_keys:
            if max_value < a_dictionary[k]:
                max_value = a_dictionary[k]
                max_value_key = k
        return max_value_key

if __name__ == "__main__":
    a_dictionary = {}
    best_key = best_score(a_dictionary)
    print("Best score: {}".format(best_key))

    best_key = best_score(None)
    print("Best score: {}".format(best_key))
