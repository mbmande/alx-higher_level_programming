#!/usr/bin/python3
"""the module"""


def write_file(filename="", text=""):
    """the method"""

    with open(filename, "w", encoding="utf-8") as fi:
        return fi.write(text)
