#!/usr/bin/python3
"""the modules"""


def append_after(filename="", search_string="", new_string=""):
    """the method"""

    inside = ""
    with open(filename) as _file:
        for line in _file:
            inside += line
            if search_string in line:
                inside += new_string
    with open(filename, "w") as _file2:
        _file2.write(inside)
