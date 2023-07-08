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
        self.assertTrue(hasattr(self.city, "state.id"))
        self.assertTrue(hasattr(self.city, "name"))

    def test_empty(self):
        """test create empty attibute"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

if __name__ == '__main__':
    unittest.main()
