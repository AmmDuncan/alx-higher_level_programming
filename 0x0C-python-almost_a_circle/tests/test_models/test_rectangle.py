#!/usr/bin/python3
"""Test Rectange Class"""
import unittest
from models.rectangle import Rectangle


class TestRectangeClass(unittest.TestCase):
    """Test suite for Rectange Class"""

    def test_attributes_hidden(self):
        """🧪 Check if attributes are hidden"""
        rect1 = Rectangle(5, 3)
        attrs = rect1.__dict__
        self.assertNotIn('width', attrs)
        self.assertNotIn('height', attrs)
        self.assertNotIn('x', attrs)
        self.assertNotIn('y', attrs)
