#!/usr/bin/python3
"""the modules"""


import json


def save_to_json_file(my_obj, filename):
    """the method"""
    with open(filename, "w") as mande:
        json.dump(my_obj, mande)
