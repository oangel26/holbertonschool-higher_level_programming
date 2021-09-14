#!/usr/bin/python3
def common_elements(set_1, set_2):
    """Function that returns a set of common elements in two sets."""
    set_common_elements = set_1 & set_2
    return set_common_elements

if __name__ == "__main__":
    set_1 = { "Python", "C", "Javascript" }
    set_2 = { "Bash", "C", "Ruby", "Perl" }
    c_set = common_elements(set_1, set_2)
    print(sorted(list(c_set)))
