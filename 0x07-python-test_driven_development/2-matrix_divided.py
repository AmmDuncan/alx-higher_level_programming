#!/usr/bin/python3
"""Module that defines matrix_divided function"""


def matrix_divided(matrix, div):
    """Function to divide all elements in a matrix

    Args:
        matrix (list): list of lists
        div (int): number to divide matrix elements by
    """
    matrix_type_err = "matrix must be a matrix (list of lists) of integers/floats"

    is_int_or_float(div, "div must be a number")
    if len(matrix) == 0:
        raise TypeError(matrix_type_err)

    row_len = len(matrix[0])
    for row in matrix:
        if type(row) != list:
            raise TypeError(matrix_type_err)
        is_same_row_len(row, row_len)
        for item in row:
            is_int_or_float(item, matrix_type_err)

    copy = [[0] * row_len for _ in matrix]
    for row_i in range(len(matrix)):
        for item_i in range(row_len):
            value = matrix[row_i][item_i]
            copy[row_i][item_i] = round(value / div, 2)

    return copy


def is_int_or_float(v, message=""):
    """check if value is int or float"""
    if type(v) not in [int, float]:
        raise TypeError(message)


def is_same_row_len(row, length):
    """check if row has same length"""
    if len(row) != length:
        raise TypeError("Each row of the matrix must have the same size")
