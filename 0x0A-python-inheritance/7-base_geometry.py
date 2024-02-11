#!/usr/bin/python3

class BaseGeometry:
    """the class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value

    if type(value) != int:
        raise TypeError("{} must be an integer".format(name))

    if value <= 2:
        raise ValueError("<name> must be greater than 0".format(name))
