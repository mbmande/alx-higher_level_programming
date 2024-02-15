#!/usr/bin/python3
"""the module"""


class Student:
    """the class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """the socond"""

        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {l: getattr(self, l) for l in attrs if hasattr(self, l)}
        return self.__dict__

    def reload_from_json(self, json):
        """the third"""
        for l, o in json.items():
            setattr(self, l, o)
