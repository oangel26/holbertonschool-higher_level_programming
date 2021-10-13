#!/usr/bin/python3
"""Module with scrpt that adds all arguments to a Python list, and then save
them to a file"""
from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
list_obj = []
try:
    my_list = load_from_json_file(filename)
    for i in range(1, len(argv)):
        my_list.append(argv[i])
    save_to_json_file(my_list, filename)
except Exception as e:
    save_to_json_file(list_obj, filename)
