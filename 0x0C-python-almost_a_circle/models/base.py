#!/usr/bin/python3
"""Module that represents class Base"""
import json
import csv


class Base:
    """Class that represents the Base Model"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class Base constructure of instances"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that returns the JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Static method that returns the list of the JSON
        string representation json_string
        """
        if json_string is None or json_string == "":
            return ([])
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        classmethod that writes the JSON string
        representation of list_objs to a file
        """
        dict_list = []
        for i in list_objs:
            dict_list.append(i.to_dictionary())
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w', encoding="UTF8") as f:
            f.write(cls.to_json_string(dict_list))

    @classmethod
    def create(cls, **dictionary):
        """
        Class method that returns an instance with all
        attributes already set.
        """
        dummy_instance = cls(1, 2, 3, 4)
        dummy_instance.update(**dictionary)
        return (dummy_instance)

    @classmethod
    def load_from_file(cls):
        """
        class method that returns a list of instances
        """
        list_of_instances = []
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, 'r', encoding="UTF8") as f:
                json_string = f.read()
                list_objs = cls.from_json_string(json_string)
                for i in list_objs:
                    list_of_instances.append(cls.create(**i))
            return list_of_instances
        except Exception as e:
            return ([])

    @classmethod
    def load_from_file_csv(cls):
        """
        class method that deserializes in CSV
        """
        list_of_instances = []
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, 'r', encoding="UTF8") as f:
                reader = csv.reader(f)
                for i in reader:
                    list_of_instances.append(i)
                return (list_of_instances)
        except Exception as e:
            return([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Class method that serializes in CSV
        """
        dict_list = []
        for i in list_objs:
            dict_list.append(i.to_dictionary())
        filename = "{}.csv".format(cls.__name__)
        with open(filename, 'w', encoding="UTF8") as f:
            writer = csv.writer(f, delimiter=':')
            for i in dict_list:
                for key, value in i.items():
                    writer.writerow([key, value])
