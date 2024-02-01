#!/usr/bin/python3
def magic_string():
    magic_string.o = getattr(magic_string, 'o', 0) + 1
    return ("BestSchool, " * (magic_string.o - 1) + "BestSchool")
