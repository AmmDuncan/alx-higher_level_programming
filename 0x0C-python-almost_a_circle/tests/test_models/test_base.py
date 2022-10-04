#!/usr/bin/python3
"""Tess Base Class"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Test Base Class"""

    def test_increments_id(self):
        """🧪 Test if id increment works"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)
        b6 = Base()
        self.assertNotEqual(b6.id, 4)

    def test_to_json_string(self):
        """🧪 Test to json static method"""
        json_s = Base.to_json_string()
        self.assertEqual(json_s, '[]')
        json_s = Base.to_json_string([{'id': 1, 'x': 2}, {'id': 2, 'x': 2}])
        self.assertEqual(json_s, '[{"id": 1, "x": 2}, {"id": 2, "x": 2}]')

    def test_from_json_string(self):
        """🧪 Test from_json_string"""
        json_s = '[{"id": 1, "x": 2}, {"id": 2, "x": 2}]'
        json_obj = Base.from_json_string(json_s)
        self.assertEqual(json_obj, [{"id": 1, "x": 2}, {"id": 2, "x": 2}])
