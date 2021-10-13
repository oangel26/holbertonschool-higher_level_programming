#!/usr/bin/python3
"""Module that appends a string to a text file"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    with open(filename, 'a',  encoding="UTF8") as f:
        data_appended = f.write(text)
    return (data_appended)


if __name__ == "__main__":
    nb_characters_added = append_write("file_append.txt",
                                       "This School is so cool!\n")
    print(nb_characters_added)
