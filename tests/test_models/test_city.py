#!/usr/bin/python3
"""unitest for city model"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.city import City


class TestUser(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test_exist(self):
        """test create exist"""
        self.assertTrue(hasattr(self.city, "email"))
        self.assertTrue(hasattr(self.city, "password"))
        self.assertTrue(hasattr(self.city, "first_name"))
        self.assertTrue(hasattr(self.city, "last_name"))

    def test_empty(self):
        """test create empty attibute"""
        self.assertEqual(self.city.email, "")
        self.assertEqual(self.city.password, "")
        self.assertEqual(self.city.first_name, "")
        self.assertEqual(self.city.last_name, "")

if __name__ == '__main__':
    unittest.main()
