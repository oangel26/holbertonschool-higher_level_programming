#!/usr/bin/python3
def uppercase(str):
    """Function that prints a string in uppercase followed by a new line."""
    for i in str:
        letter = i
        if ord(i) in range(97, 123):
            letter = chr(ord(i) - 32)
        print("{}".format(letter), end="")
    print()
