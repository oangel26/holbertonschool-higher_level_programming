#!/usr/bin/python
"""Program that prints the result of the addition of all arguments"""
if __name__ == "__main__":
    from sys import argv
    result = 0
    if len(argv) > 1:
        for i in argv[1:]:
            result += int(i)
    else:
        pass
    print("{}".format(result))
