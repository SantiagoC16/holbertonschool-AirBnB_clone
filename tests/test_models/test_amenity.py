#!/usr/bin/python3
"""unitest for amenity model"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class TestUser(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_exist(self):
        """test create exist"""
        self.assertTrue(hasattr(self.amenity, "email"))
        self.assertTrue(hasattr(self.amenity, "password"))
        self.assertTrue(hasattr(self.amenity, "first_name"))
        self.assertTrue(hasattr(self.amenity, "last_name"))

    def test_empty(self):
        """test create empty attibute"""
        self.assertEqual(self.amenity.email, "")
        self.assertEqual(self.amenity.password, "")
        self.assertEqual(self.amenity.first_name, "")
        self.assertEqual(self.amenity.last_name, "")

if __name__ == '__main__':
    unittest.main()
