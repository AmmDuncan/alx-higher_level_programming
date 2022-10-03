#!/usr/bin/python3
"""Test "square" Module"""
import unittest
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """Test Square Class"""

    def test_instantiation(self):
        """🧪 Test square instantiation"""
        s = Square(5, 2, 1, 32)
        self.assertEqual(str(s), "[Square] (32) 2/1 - 5/5")

    def test_size_validation(self):
        """🧪 Test validation on size property"""
        s = Square(5, 2, 1, 32)
        with self.assertRaises(TypeError):
            s.size = "size"
        with self.assertRaises(ValueError):
            s.size = 0
        with self.assertRaises(ValueError):
            s.size = -3
