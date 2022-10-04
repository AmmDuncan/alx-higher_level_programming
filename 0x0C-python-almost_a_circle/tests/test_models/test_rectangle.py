#!/usr/bin/python3
"""Test Rectange Class"""
import unittest
import json
from models.rectangle import Rectangle


class TestRectangeClass(unittest.TestCase):
    """Test suite for Rectange Class"""

    def test_instantiation_validation(self):
        """🧪 Check if instantiation validation raises appropriate errors"""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle("5", 3)
        with self.assertRaises(TypeError):
            Rectangle(5, "3")
        with self.assertRaises(TypeError):
            Rectangle(5, 3, "0", 0)
        with self.assertRaises(TypeError):
            Rectangle(5, 3, 0, "0")
        with self.assertRaises(ValueError):
            Rectangle(0, 3, 0, 0)
        with self.assertRaises(ValueError):
            Rectangle(5, 0, 0, 0)
        with self.assertRaises(ValueError):
            Rectangle(5, 3, -1, 0)
        with self.assertRaises(ValueError):
            Rectangle(-1, 2, -1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, -2, -1, 0)

    def test_attributes_hidden(self):
        """🧪 Check if attributes are hidden"""
        rect1 = Rectangle(5, 3)
        attrs = rect1.__dict__
        self.assertNotIn('width', attrs)
        self.assertNotIn('height', attrs)
        self.assertNotIn('x', attrs)
        self.assertNotIn('y', attrs)

    def test_width_setter(self):
        """🧪 Test width setter"""
        r = Rectangle(5, 3, 0, 0)
        with self.assertRaises(TypeError):
            r.width = "a"
        with self.assertRaises(ValueError):
            r.width = 0
        with self.assertRaises(ValueError):
            r.width = -4
        # Valid
        r.width = 4

    def test_height_setter(self):
        """🧪 Test height setter"""
        r = Rectangle(5, 3, 0, 0)
        with self.assertRaises(TypeError):
            r.height = "a"
        with self.assertRaises(ValueError):
            r.height = 0
        with self.assertRaises(ValueError):
            r.height = -4
        # Valid
        r.height = 3

    def test_x_setter(self):
        """🧪 Test x setter"""
        r = Rectangle(5, 3, 0, 0)
        with self.assertRaises(TypeError):
            r.x = "a"
        with self.assertRaises(ValueError):
            r.x = -4
        # Valid
        r.x = 2

    def test_y_setter(self):
        """🧪 Test y setter"""
        r = Rectangle(5, 3, 0, 0)
        with self.assertRaises(TypeError):
            r.y = "a"
        with self.assertRaises(ValueError):
            r.y = -4
        # Valid
        r.y = 2

    def test_area(self):
        """🧪 Test area method"""
        r = Rectangle(5, 3, 0, 0)
        self.assertEqual(r.area(), 15)
        r.width = 7
        self.assertEqual(r.area(), 21)
        r.height = 4
        self.assertEqual(r.area(), 28)

    def test_str(self):
        """🧪 Test area method"""
        r = Rectangle(5, 3, 0, 0, 101)
        self.assertEqual(str(r), "[Rectangle] (101) 0/0 - 5/3")

    def test_update(self):
        """🧪 Test update method"""
        r = Rectangle(5, 3, 0, 0, 101)
        self.assertEqual(str(r), "[Rectangle] (101) 0/0 - 5/3")
        r.update(64)
        self.assertEqual(str(r), "[Rectangle] (64) 0/0 - 5/3")
        r.update(64, 8)
        self.assertEqual(str(r), "[Rectangle] (64) 0/0 - 8/3")
        r.update(64, 8, 4)
        self.assertEqual(str(r), "[Rectangle] (64) 0/0 - 8/4")
        r.update(64, 8, 4, 2)
        self.assertEqual(str(r), "[Rectangle] (64) 2/0 - 8/4")
        r.update(64, 8, 4, 2, 1)
        self.assertEqual(str(r), "[Rectangle] (64) 2/1 - 8/4")
        r.update(id=46)
        self.assertEqual(str(r), "[Rectangle] (46) 2/1 - 8/4")
        r.update(width=20, height=12)
        self.assertEqual(str(r), "[Rectangle] (46) 2/1 - 20/12")
        r.update(x=3, y=4)
        self.assertEqual(str(r), "[Rectangle] (46) 3/4 - 20/12")

    def test_to_dictionary(self):
        """🧪 Test to_dictionary method"""
        r = Rectangle(5, 4,  2, 1, 32)
        self.assertDictEqual(r.to_dictionary(), {
                             'id': 32, 'width': 5,
                             'height': 4, 'x': 2, 'y': 1})

    def test_create_instance(self):
        """🧪 Test create method"""
        r1 = Rectangle(5, 3, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(str(r1), str(r2))

    def test_save_to_file(self):
        """🧪 Test save to file"""
        r1 = Rectangle(5, 3, 0, 0, 23)
        r2 = Rectangle(5, 2, 1, 1, 24)
        lst = [r1, r2]
        dict_list = [*map(lambda x: x.to_dictionary(), lst)]
        Rectangle.save_to_file(lst)
        with open('Rectangle.json', 'r') as file:
            content = file.read()
            self.assertListEqual(dict_list, json.loads(content))
