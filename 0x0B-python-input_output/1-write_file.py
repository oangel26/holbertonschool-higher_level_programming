#!/usr/bin/python3
"""Module that writes a string to a text file"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file (UTF8)
    and returns the number of characters written
    """
    with open(filename, 'w',  encoding="UTF8") as f:
        data_written = f.write(text)
    return (data_written)


if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt",
                               "This School is so cool!\n")
    print(nb_characters)
