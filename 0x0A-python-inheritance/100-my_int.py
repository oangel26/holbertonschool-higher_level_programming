#!/usr/bin/python3
""" Module that represents class MyInt """


class MyInt(int):
    """ Class that represents integer and inherits from int"""

    def __eq__(self, int):
        return self.value == int

if __name__ == "__main__":
    my_i = MyInt(3)
    print(my_i)
    print(my_i == 3)
    print(my_i != 3)
