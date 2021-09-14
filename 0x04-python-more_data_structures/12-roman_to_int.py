#!/usr/bin/python3
def roman_to_int(roman_string):
    """Functon that converts a Roman numeral to an integer."""
    if type(roman_string) != str or roman_string is None:
        return 0
    else:
        roman_dict = {'I': 1, 'V': 5,'X': 10, 'L': 50,'C': 100,'D': 500}
        roman_list = list(roman_string)
        number = 0
        for i in range(len(roman_list) - 1):
            if roman_dict[roman_list[i]] >= roman_dict[roman_list[i + 1]]:
                number += roman_dict[roman_list[i]]
            else:
                number = number - roman_dict[roman_list[i]]
        number += roman_dict[roman_list[len(roman_list) - 1]]
        return number

if __name__ == "__main__":
    """ Roman to Integer test file
    """
    roman_number = "X"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "VII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "IX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "LXXXVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "DCCVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))
