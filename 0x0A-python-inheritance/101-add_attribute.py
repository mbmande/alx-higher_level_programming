#!/usr/bin/python
"""the module"""


def add_attribute(obj, att, value):
    """the attributes

    Args:
        obj (any): ===
        att (str): =====
        value (any): ====
    Raises:
        TypeError: ======
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
