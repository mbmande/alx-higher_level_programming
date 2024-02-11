#!/usr/bin/python
"""the module"""

def add_attribute(obj, att, value):
    """the attributes"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
