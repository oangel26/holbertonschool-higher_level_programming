#!/usr/bin/python3
def print_last_digit(number):
    """function that prints the last digit of a number."""
    num = str(number)
    print("{}".format(int(num[-1])), end="")
    return int(num[-1])
