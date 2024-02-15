#!/usr/bin/python3
"""the module"""


import json


def load_from_json_file(filename):
    """the method"""

    with open(filename) as mande:
        return json.load(mande)
