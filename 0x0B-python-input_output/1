#!/usr/bin/python3
"""the module"""


def pascal_triangle(n):
    """the method"""

    if n <= 0:
        return []

    mande = [[1]]
    while len(mande) != n:
        man = mande[-1]
        t = [1]
        for i in range(len(man) - 1):
            t.append(man[i] + man[i + 1])
        t.append(1)
        mande.append(t)
    return mande
