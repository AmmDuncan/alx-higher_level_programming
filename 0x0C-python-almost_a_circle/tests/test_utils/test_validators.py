#!/usr/bin/python3
"""Test validation utility functions"""
import unittest
from utils import validators


class TestValidationUtils(unittest.TestCase):
    """Test cases for validation utility functions"""

    def test_is_integer(self):
        """🧪 Test if is_integer raises exception on failure"""
        with self.assertRaises(TypeError):
            validators.is_integer("a")
        with self.assertRaises(TypeError):
            validators.is_integer({})
        with self.assertRaises(TypeError):
            validators.is_integer([1])
        with self.assertRaises(TypeError):
            validators.is_integer((1,))
        # Valid
        self.assertEqual(None, validators.is_integer(1))
        self.assertEqual(None, validators.is_integer(-8))

    def test_is_non_negative_integer(self):
        """🧪 Test if is_non_negative_integer raises exception on failure"""
        # assert value it integer first
        with self.assertRaises(TypeError):
            validators.is_non_negative_integer("a")
        with self.assertRaises(TypeError):
            validators.is_non_negative_integer({})
        with self.assertRaises(TypeError):
            validators.is_non_negative_integer([1])
        with self.assertRaises(TypeError):
            validators.is_non_negative_integer((1,))
        # Check Value
        with self.assertRaises(ValueError):
            validators.is_non_negative_integer(-8)
        # Valid
        self.assertEqual(None, validators.is_non_negative_integer(1))
        self.assertEqual(None, validators.is_non_negative_integer(0))

    def test_is_positive_integer(self):
        """🧪 Test if is_positive_integer raises exception on failure"""
        # assert value it integer first
        with self.assertRaises(TypeError):
            validators.is_positive_integer("a")
        with self.assertRaises(TypeError):
            validators.is_positive_integer({})
        with self.assertRaises(TypeError):
            validators.is_positive_integer([1])
        with self.assertRaises(TypeError):
            validators.is_positive_integer((1,))
        # Check Value
        with self.assertRaises(ValueError):
            validators.is_positive_integer(-8)
        with self.assertRaises(ValueError):
            validators.is_positive_integer(0)
        # Valid
        self.assertEqual(None, validators.is_positive_integer(1))
        self.assertEqual(None, validators.is_positive_integer(26))
