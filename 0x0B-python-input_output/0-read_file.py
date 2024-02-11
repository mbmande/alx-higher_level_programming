#!/usr/bin/python3
"""the module"""


def read_file(filename=""):
    """the mothod"""
    with open(filename, encoding="utf-8") as fi:
        print(fi.read(), end="")
