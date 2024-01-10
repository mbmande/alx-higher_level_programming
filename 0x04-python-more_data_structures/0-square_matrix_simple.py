#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_d = []
    for line in matrix:
        square_d.append([c**2 for c in line])
    return square_d
