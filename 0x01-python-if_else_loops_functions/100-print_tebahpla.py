#!/usr/bin/python3
for i in reversed(range(97, 123)):
    letter = chr(i - 32)
    if i % 2 == 0:
        letter = chr(i)
    print("{}".format(letter), end="")
