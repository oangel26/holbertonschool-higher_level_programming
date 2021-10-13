#!/usr/bin/python3
""" Module with functions that reads a text file """


def read_file(filename=""):
    """Function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="UTF8") as f:
        read_data = f.read()
    print(read_data, end="")


if __name__ == "__main__":
    read_file("my_file_0.txt")
