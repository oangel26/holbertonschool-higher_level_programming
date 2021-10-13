#!/usr/bin/python3
"""Module that creates an Object form JSON file"""
import json


def load_from_json_file(filename):
    """Function that creates an Object from a “JSON file”"""
    with open(filename, 'r', encoding="UTF8") as f:
        jason_ofile = json.load(f)
    return jason_ofile
