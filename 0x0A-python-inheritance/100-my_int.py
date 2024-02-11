#!/usr/bin/python3
"""the module"""


class MyInt(int):
    """the class"""
    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
