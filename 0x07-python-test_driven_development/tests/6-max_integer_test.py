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

    def test_single_integer(self):
        """test with single integer list"""
        self.assertAlmostEqual(max_integer([2]), 2)

    def test_with_negative(self):
        """test with list containing negative integer"""
        self.assertAlmostEqual(max_integer([3, 4, -1, 8]), 8)

    def test_with_all_negative(self):
        """test with list containing all negative integer"""
        self.assertAlmostEqual(max_integer([-1, -5, -8]), -1)
