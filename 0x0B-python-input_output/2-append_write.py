#!/usr/bin/python3
"""the module"""


def append_write(filename="", text=""):
    """the mothod"""
    with open(filename, "a", encoding="utf-8") as fi:
        return fi.write(text)
