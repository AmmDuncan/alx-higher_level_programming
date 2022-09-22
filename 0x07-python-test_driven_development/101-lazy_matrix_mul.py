#!/usr/bin/python3
"""Multiply two matrices"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    mat_a = np.array(m_a)
    mat_b = np.array(m_b)
    return np.matmul(mat_a, mat_b)


def validate_args(val1, val2, name1="m_a", name2="m_b"):
    """Validate matrix_mul params"""
    checks = [
        is_list,
        is_list_of_lists,
        is_not_empty,
        contains_only_int_or_float,
        each_row_has_same_size
    ]
    for check in checks:
        check(val1, name1)
        check(val2, name2)

    # m_a cols should be equal to m_b rows for matrix_mul
    # to be possible
    if len(val1[0]) != len(val2):
        raise ValueError("m_a and m_b can't be multiplied")


def is_list(value, name):
    """Check if value is of type list"""
    if type(value) != list:
        raise TypeError("{} must be a list".format(name))


def is_list_of_lists(value, name):
    """Check if value is a list containing lists"""
    if len(value) and type(value[0]) != list:
        raise TypeError("{} must be a list of lists".format(name))


def is_not_empty(value, name):
    """Check if value is not empty"""
    if not len(value) or not len(value[0]):
        raise ValueError("{} can't be empty".format(name))


def contains_only_int_or_float(value, name):
    """Check if matrix contains only integers or floats"""
    for row in value:
        for item in row:
            if type(item) != int and type(item) != float:
                raise TypeError(
                    "{} should contain only integers or floats".format(name))


def each_row_has_same_size(value, name):
    """Check if each row of matrix has same length"""
    row_len = len(value[0])
    for row in value:
        if len(row) != row_len:
            raise TypeError(
                "each row of {} must be of the same size".format(name)
            )
