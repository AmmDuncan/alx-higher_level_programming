#!/usr/bin/python3
"""Test "square" Module"""
import unittest
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """Test Square Class"""

    def test_instantiation(self):
        """🧪 Test square instantiation"""
        s = Square(5, 2, 1, 32)
        self.assertEqual(str(s), "[Square] (32) 2/1 - 5")

    def test_size_validation(self):
        """🧪 Test validation on size property"""
        s = Square(5, 2, 1, 32)
        with self.assertRaises(TypeError):
            s.size = "size"
        with self.assertRaises(ValueError):
            s.size = 0
        with self.assertRaises(ValueError):
            s.size = -3

    def test_to_dictionary(self):
        """🧪 Test to_dictionary method"""
        s = Square(5, 2, 1, 32)
        self.assertDictEqual(s.to_dictionary(), {
                             'id': 32, 'size': 5, 'x': 2, 'y': 1})

    def test_create_instance(self):
        """🧪 Test create method"""
        s1 = Square(5, 1, 1)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(str(s1), str(s2))
