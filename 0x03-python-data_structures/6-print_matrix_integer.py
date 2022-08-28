#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    str = "{:d} {:d} {:d}"
    for row in matrix:
        if len(row):
            print(str.format(*row))
        else:
            print()
