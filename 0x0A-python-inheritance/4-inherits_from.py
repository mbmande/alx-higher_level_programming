#!/usr/bin/python3
"""the module"""


def inherits_from(obj, a_class):
    "it checks if it's an instance of a class directly or indirectly"

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
