#!/usr/bin/python3
"""Module of class Student"""


class Student:
    """Class that represents an student"""

    def __init__(self, first_name, last_name, age):
        """Constructor of Student objects"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method that retrieves a dictionary
        representation of a Student instance
        """
        new_dict = {}
        if type(attrs) is list:
            for i in attrs:
                if type(i) is str:
                    if hasattr(self, i):
                        new_dict[i] = getattr(self, i)
                else:
                    return (self.__dict__)
        else:
            return (self.__dict__)
        return (new_dict)

