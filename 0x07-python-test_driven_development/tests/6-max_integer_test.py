#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """empty list"""
        self.assertAlmostEqual(max_integer([]), None)

    def test_non_integer(self):
        """non integer values"""
        with self.assertRaises(TypeError):
            max_integer([1, 'a', 3])

    def test_all_integer(self):
        """test with list of integers"""
        self.assertAlmostEqual(max_integer([1, 2, 6, 3]), 6)
