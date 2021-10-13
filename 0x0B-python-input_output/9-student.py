#!/usr/bin/python3
"""Module of class Student"""


class Student:
    """Class that represents an student"""

    def __init__(self, first_name, last_name, age):
        """Constructor of Student objects"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Public method that retrieves a dictionary
        representation of a Student instance
        """
        return (self.__dict__)
