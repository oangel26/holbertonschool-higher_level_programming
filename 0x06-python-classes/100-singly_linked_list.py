#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Module which represents single linked list """


class Node:
    """ Class that defines a node of a singly linked list """
    def __init__(self, data, next_node=None):
        """ Constructor of the Node:
        Args:
        data (int): data in node..
        next_node (Node): next node.

        Raises:
        TypeError: if data is no integer
        TyperError: if next node is not a Node object

        """
        self.__data = data
        self.__next_node = next_node

        @property
        def data(self):
            return self.__data

        @data.setter
        def data(self, value):
            if type(value) is not int:
                raise TypeError("data must be an integer")
            else:
                self.__data = value

        @property
        def next_node(self):
            return self.__next_node

        @next_node.setter
        def next_node(self, value):
            if value == None or value.__name__ == Node:
                self.__next_node = value
            else:
                raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """ Class that defines a singly linked list """
    def __init__(self):
        """ Constructor of singly linked list

        """
        self.__head = None

    def sorted_insert(self, value):
        """ Public instance method that inserts
        a new Node into the correct sorted position in the list
        """
        new_node = Node(value, None)
        if self.__head = None:
            self.__head = new_node
        else:
            for i in 
            

if __name__ == "__main__":

    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)
    
