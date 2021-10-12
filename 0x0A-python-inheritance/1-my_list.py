#!/usr/bin/python3
""" Module of class which inherits form list """


class MyList(list):
    """ class MyList that inherits form list """

    def print_sorted(self):
        """ public instance method that prints the list,
        but sorted (ascending sort)
        """
        print(sorted(self))


if __name__ == "__main__":
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)
