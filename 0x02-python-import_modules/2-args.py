#!/usr/bin/python3
"""Program that prints the number of the and the list of its arguments"""
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("{} argument:".format(len(argv) - 1))
        print("{}: {}".format(len(argv) - 1, argv[1]))
    else:
        print("{} arguments:".format(len(argv) - 1))
        counter = 0
        for i in argv[1:]:
            counter += 1
            print("{}: {}".format(counter, i))
