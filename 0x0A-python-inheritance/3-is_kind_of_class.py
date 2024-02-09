#!/usr/bin/python3
"""the module"""


def is_kind_of_class(obj, a_class):
    """it checks the instance of a class"""

    if isinstance(obj, a_class):
        return True
    return False
