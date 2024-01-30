#!/usr/bin/python3
"""text indentation"""


def text_indentation(text):

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    o = 0
    while o < len(text) and text[o] == ' ':
        o += 1

    while o < len(text):
        print(text[o], end="")

        if text[o] == "\n" or text[o] in ".?:":
            if text[o] in ".?":
                print("\n")
            o += 1
            while o < len(text) and text[o] == ' ':
                o += 1
            continue
        o += 1
